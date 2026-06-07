import re
import pandas as pd
from datetime import datetime

def parse_ucl_file(path):
    rows = []
    current_date = None
    current_stage = None
    current_matchday = None

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            # Detect stage + matchday
            if line.startswith("▪"):
                current_stage = line.replace("▪", "").strip().split(",")[0]
                if "Matchday" in line:
                    current_matchday = line.split("Matchday")[1].strip()
                continue

            # Detect date line
            date_match = re.match(r"([A-Za-z]{3} [A-Za-z]{3} \d{1,2} \d{4})", line)
            if date_match:
                current_date = datetime.strptime(date_match.group(1), "%a %b %d %Y").date()
                continue

            # Detect match line
            match_regex = r"(\d{2}:\d{2})\s+(.*?)\s+v\s+(.*?)\s+(\d+)-(\d+)\s+\((\d+)-(\d+)\)"
            m = re.match(match_regex, line)
            if m:
                time, home, away, hg, ag, hthg, htag = m.groups()
                rows.append({
                    "date": current_date,
                    "time": time,
                    "home_team": home,
                    "away_team": away,
                    "home_goals": int(hg),
                    "away_goals": int(ag),
                    "ht_home_goals": int(hthg),
                    "ht_away_goals": int(htag),
                    "stage": current_stage,
                    "matchday": current_matchday
                })

    return pd.DataFrame(rows)

df = parse_ucl_file("/home/sudhir/OneDrive/prof/comsci/ArtificialIntelligence/Machine Learning/sample-data/ucl_2025_26.txt")

df.to_csv("/home/sudhir/OneDrive/prof/comsci/ArtificialIntelligence/Machine Learning/sample-data/ucl_2025_26_clean.csv", index=False)

print(df.head())
