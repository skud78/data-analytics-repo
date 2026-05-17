import csv

MASTER_CSV = "/home/sudhir/OneDrive/pers/ctl/project-plans/master-plans.csv"

with open(MASTER_CSV, "r") as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader, start=1):
        if len(row) != 17:
            print(f"Line {i} has {len(row)} fields instead of 17")
            print(row)
            break
