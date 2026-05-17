





import pandas as pd
from datetime import datetime
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import os


MASTER_CSV = "/home/sudhir/OneDrive/pers/ctl/project-plans/master-plans.csv"
OUTPUT_XML = "/home/sudhir/OneDrive/pers/ctl/project-plans/projectlibre_import.xml"

# -----------------------------
# Load CSV
# -----------------------------
df = pd.read_csv(MASTER_CSV, dtype=str).fillna("")
df.columns = df.columns.str.strip()

# Convert dates
def parse_date(s):

    if not s:
        return None
    for fmt in ("%Y/%m/%d","%Y-%m-%d"):
        try:
            return datetime.strptime(s, fmt)
        except:
            pass
        return None

df["StartDate_dt"] = df["StartDate"].apply(parse_date)
df["EndDate_dt"] = df["EndDate"].apply(parse_date)

# Duration in hours
def parse_int(s, default=0):
    try:
        return int(float(s))
    except:
        return default

df["DurationDays_int"] = df["DurationDays"].apply(lambda x: parse_int(x, 0))
df["PercentComplete_int"] = df["PercentComplete"].apply(lambda x: parse_int(x, 0))

# -----------------------------
# Build hierarchy
# -----------------------------
class Node:
    def __init__(self, name, level, kind):
        self.name = name
        self.level = level
        self.kind = kind
        self.children = []
        self.rows = []
        self.uid = None
        self.id = None
        self.wbs = ""
        self.outline = ""
        self.start = None
        self.finish = None
        self.duration_hours = 0
        self.percent_complete = 0

    def add_child(self, child):
        self.children.append(child)

domains = []
domain_map = {}

for _, row in df.iterrows():
    dom = row["Domain"]
    sub = row["Subdomain"]
    prog = f"{row['ProjectID']}::{row['ProjectName']}"

    # Domain
    if dom not in domain_map:
        d = Node(dom, 1, "domain")
        domains.append(d)
        domain_map[dom] = {"node": d, "subs": {}}
    dnode = domain_map[dom]["node"]

    # Subdomain
    if sub not in domain_map[dom]["subs"]:
        s = Node(sub, 2, "subdomain")
        dnode.add_child(s)
        domain_map[dom]["subs"][sub] = {"node": s, "progs": {}}
    snode = domain_map[dom]["subs"][sub]["node"]

    # Program
    if prog not in domain_map[dom]["subs"][sub]["progs"]:
        pname = row["ProjectName"] if row["ProjectName"] else row["ProjectID"]
        p = Node(pname, 3, "program")
        snode.add_child(p)
        domain_map[dom]["subs"][sub]["progs"][prog] = {"node": p}
    pnode = domain_map[dom]["subs"][sub]["progs"][prog]["node"]

    # Task
    t = Node(row["TaskName"], 4, "task")
    t.rows.append(row)
    t.start = row["StartDate_dt"]
    t.finish = row["EndDate_dt"]

    if row["DurationDays_int"] > 0:
        t.duration_hours = row["DurationDays_int"] * 8
    elif t.start and t.finish:
        days = (t.finish - t.start).days or 1
        t.duration_hours = days * 8
    else:
        t.duration_hours = 8

    t.percent_complete = row["PercentComplete_int"]
    pnode.add_child(t)

# -----------------------------
# Compute summary dates
# -----------------------------
def compute(node):
    if not node.children:
        return node.start, node.finish

    starts, finishes = [], []
    for c in node.children:
        cs, cf = compute(c)
        if cs: starts.append(cs)
        if cf: finishes.append(cf)

    if starts: node.start = min(starts)
    if finishes: node.finish = max(finishes)

    if node.start and node.finish:
        days = (node.finish - node.start).days or 1
        node.duration_hours = days * 8

    # summary percent complete = avg of leaf tasks
    leaf = []
    def collect(n):
        if not n.children and n.kind == "task":
            leaf.append(n.percent_complete)
        for ch in n.children:
            collect(ch)
    collect(node)

    node.percent_complete = sum(leaf)//len(leaf) if leaf else 0
    return node.start, node.finish

for d in domains:
    compute(d)

# -----------------------------
# Assign WBS + UID
# -----------------------------
all_nodes = []

def assign(node, prefix):
    node.outline = ".".join(str(x) for x in prefix)
    node.wbs = node.outline
    all_nodes.append(node)

    i = 1
    for ch in node.children:
        assign(ch, prefix + [i])
        i += 1

for i, d in enumerate(domains, start=1):
    assign(d, [i])

for i, n in enumerate(all_nodes, start=1):
    n.uid = i
    n.id = i

# -----------------------------
# Build XML
# -----------------------------
NS = "http://schemas.microsoft.com/project"
ET.register_namespace("", NS)
proj = ET.Element("Project", xmlns=NS)

def add(tag, val):
    e = ET.SubElement(proj, tag)
    e.text = str(val)

project_start = min([n.start for n in all_nodes if n.start])
project_finish = max([n.finish for n in all_nodes if n.finish])

add("SaveVersion", 14)
add("Name", "Unified-Portfolio")
add("Title", "Unified-Portfolio")
add("ScheduleFromStart", 1)
add("StartDate", project_start.strftime("%Y-%m-%dT08:00:00"))
add("FinishDate", project_finish.strftime("%Y-%m-%dT17:00:00"))
add("MinutesPerDay", 480)
add("MinutesPerWeek", 2400)
add("DaysPerMonth", 20)
add("CalendarUID", 1)

ET.SubElement(proj, "ExtendedAttributes")

# Calendar (Standard)
cals = ET.SubElement(proj, "Calendars")
cal = ET.SubElement(cals, "Calendar")
ET.SubElement(cal, "UID").text = "1"
ET.SubElement(cal, "Name").text = "Standard"
ET.SubElement(cal, "IsBaseCalendar").text = "1"
wd = ET.SubElement(cal, "WeekDays")

def add_wd(day, working):
    w = ET.SubElement(wd, "WeekDay")
    ET.SubElement(w, "DayType").text = str(day)
    ET.SubElement(w, "DayWorking").text = "1" if working else "0"
    if working:
        wts = ET.SubElement(w, "WorkingTimes")
        for ft, tt in [("08:00:00","12:00:00"),("13:00:00","17:00:00")]:
            wt = ET.SubElement(wts, "WorkingTime")
            ET.SubElement(wt, "FromTime").text = ft
            ET.SubElement(wt, "ToTime").text = tt

add_wd(1, False)
for d in [2,3,4,5,6]:
    add_wd(d, True)
add_wd(7, False)

# Tasks
tasks = ET.SubElement(proj, "Tasks")

def fmt(dt, start=True):
    if not dt:
        return project_start.strftime("%Y-%m-%dT08:00:00")
    return dt.strftime("%Y-%m-%dT08:00:00") if start else dt.strftime("%Y-%m-%dT17:00:00")

for n in all_nodes:
    t = ET.SubElement(tasks, "Task")
    ET.SubElement(t, "UID").text = str(n.uid)
    ET.SubElement(t, "ID").text = str(n.id)
    ET.SubElement(t, "Name").text = n.name
    ET.SubElement(t, "WBS").text = n.wbs
    ET.SubElement(t, "OutlineNumber").text = n.outline
    ET.SubElement(t, "OutlineLevel").text = str(n.level)
    ET.SubElement(t, "Start").text = fmt(n.start, True)
    ET.SubElement(t, "Finish").text = fmt(n.finish, False)
    ET.SubElement(t, "Duration").text = f"PT{int(n.duration_hours)}H0M0S"
    ET.SubElement(t, "DurationFormat").text = "39"
    ET.SubElement(t, "Summary").text = "1" if n.children else "0"
    ET.SubElement(t, "PercentComplete").text = str(n.percent_complete)
    ET.SubElement(t, "PercentWorkComplete").text = str(n.percent_complete)
    ET.SubElement(t, "CalendarUID").text = "-1"

# Resources (only Unassigned)
res = ET.SubElement(proj, "Resources")
r = ET.SubElement(res, "Resource")
ET.SubElement(r, "UID").text = "0"
ET.SubElement(r, "ID").text = "0"
ET.SubElement(r, "Name").text = "Unassigned"
ET.SubElement(r, "Type").text = "1"
ET.SubElement(r, "IsNull").text = "0"
ET.SubElement(r, "AvailabilityPeriods")

# Empty Assignments
ET.SubElement(proj, "Assignments")

# -----------------------------
# Write XML
# -----------------------------
xml_str = minidom.parseString(ET.tostring(proj)).toprettyxml(indent="  ")
output_path = os.path.abspath(OUTPUT_XML)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(xml_str)

print("XML written to:", output_path)
