import pandas as pd
from datetime import datetime

# ---------------------------------------------------------
# CONFIG
# ---------------------------------------------------------

MASTER_CSV = "MASTER_PORTFOLIO.csv"
OUTPUT_CSV = "PROJECTLIBRE_IMPORT.csv"

# ProjectLibre date format
PL_DATE_FORMAT = "%d/%m/%y"

# ---------------------------------------------------------
# LOAD MASTER CSV
# ---------------------------------------------------------

df = pd.read_csv(MASTER_CSV)

# ---------------------------------------------------------
# CREATE NUMERIC IDs FOR PROJECTLIBRE
# ---------------------------------------------------------

df = df.reset_index().rename(columns={"index": "ID"})
df["ID"] = df["ID"] + 1  # ProjectLibre IDs start at 1

# ---------------------------------------------------------
# MAP TASKID → NUMERIC ID (for predecessors)
# ---------------------------------------------------------

taskid_to_numeric = dict(zip(df["TaskID"], df["ID"]))

def map_predecessor(dep):
    if pd.isna(dep) or dep == "":
        return ""
    return ",".join(str(taskid_to_numeric[d.strip()]) for d in dep.split(","))

df["Predecessors"] = df["DependencyTaskID"].apply(map_predecessor)

# ---------------------------------------------------------
# FORMAT DURATION FOR PROJECTLIBRE
# ---------------------------------------------------------

df["Duration"] = df["DurationDays"].astype(str) + "d"

# ---------------------------------------------------------
# FORMAT DATES FOR PROJECTLIBRE
# ---------------------------------------------------------

def format_date(d):
    if pd.isna(d) or d == "":
        return ""
    return datetime.strptime(str(d), "%Y-%m-%d").strftime(PL_DATE_FORMAT)

df["Start"] = df["StartDate"].apply(format_date)
df["Finish"] = df["EndDate"].apply(format_date)

# ---------------------------------------------------------
# RESOURCE NAMES
# ---------------------------------------------------------

df["ResourceNames"] = df["AssignedTo"].fillna("")

# ---------------------------------------------------------
# SELECT PROJECTLIBRE COLUMNS
# ---------------------------------------------------------

pl_df = df[[
    "ID",
    "TaskName",
    "Duration",
    "Start",
    "Finish",
    "PercentComplete",
    "Predecessors",
    "ResourceNames"
]]

pl_df = pl_df.rename(columns={
    "TaskName": "Name"
})

# ---------------------------------------------------------
# EXPORT
# ---------------------------------------------------------

pl_df.to_csv(OUTPUT_CSV, index=False)

print("ProjectLibre CSV generated:", OUTPUT_CSV)
