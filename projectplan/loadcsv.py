import pandas as pd
from pathlib import Path

# ---------------------------------------------------------
# 1. Define the canonical template schema
# ---------------------------------------------------------
TEMPLATE_COLUMNS = [
    "Domain","Subdomain","ProjectID","ProjectName","TaskID","TaskName",
    "TaskDescription","StartDate","EndDate","DurationDays","DependencyTaskID",
    "AssignedTo","Priority","Status","PercentComplete","Category","Notes"
]

# ---------------------------------------------------------
# 2. Load and normalize all CSVs in a directory
# ---------------------------------------------------------
def load_portfolio_directory(base_path):
    base = Path(base_path)
    csv_files = list(base.glob("*.csv"))

    frames = []

    for file in csv_files:
        df = pd.read_csv(file)

        # Add missing columns
        for col in TEMPLATE_COLUMNS:
            if col not in df.columns:
                df[col] = None

        # Reorder columns
        df = df[TEMPLATE_COLUMNS]

        # Track source file
        df["SourceFile"] = file.name

        frames.append(df)

    # Merge all CSVs
    master = pd.concat(frames, ignore_index=True)

    return master

# ---------------------------------------------------------
# 3. Create a Gantt-ready export
# ---------------------------------------------------------
def create_gantt_export(df):
    gantt = df.copy()

    # GanttProject expects:
    # TaskID, TaskName, StartDate, EndDate, Duration, Completion, Predecessors

    gantt_export = pd.DataFrame({
        "ID": gantt["TaskID"],
        "Name": gantt["TaskName"],
        "Start": gantt["StartDate"],
        "End": gantt["EndDate"],
        "Duration": gantt["DurationDays"],
        "Completion": gantt["PercentComplete"],
        "Predecessors": gantt["DependencyTaskID"],
        "Project": gantt["ProjectName"],
        "Domain": gantt["Domain"],
        "Subdomain": gantt["Subdomain"]
    })

    return gantt_export

# ---------------------------------------------------------
# 4. Run the pipeline
# ---------------------------------------------------------
if __name__ == "__main__":
    base_path = "/Users/Sudhir/OneDrive/Portfolio/"

    master_df = load_portfolio_directory(base_path)
    print("Loaded portfolio:", master_df.shape)

    gantt_df = create_gantt_export(master_df)
    print("Gantt export:", gantt_df.shape)

    # Save outputs
    master_df.to_csv(base_path + "MASTER_PORTFOLIO_COMBINED.csv", index=False)
    gantt_df.to_csv(base_path + "GANTT_IMPORT.csv", index=False)
