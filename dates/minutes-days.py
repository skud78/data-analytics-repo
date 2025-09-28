import pandas as pd

# === CONFIG ===
input_csv = r'C:\Users\469991\MTN Group\TES Solutions Architects - Documents\General\Reporting\Feasibility\OLA-2025\sample-output-audit-data\august-css.csv'       # Replace with your actual file path
output_csv = r'C:\Users\469991\MTN Group\TES Solutions Architects - Documents\General\Reporting\Feasibility\OLA-2025\sample-output-audit-data\output_file.csv'     # Where to save the result
minutes_column = 'total_minutes'   # Column name in your CSV

# === FORMATTER FUNCTIONS ===
def to_decimal_days(minutes):
    try:
        return round(float(minutes) / 1440, 2)
    except:
        return None

def to_dhm_format(minutes):
    try:
        total_minutes = int(float(minutes))
        days = total_minutes // 1440
        remainder = total_minutes % 1440
        hours = remainder // 60
        mins = remainder % 60
        return f"{days}d {hours}h {mins}m"
    except:
        return None

# === PROCESSING ===
df = pd.read_csv(input_csv)

df['business_days_decimal'] = df[minutes_column].apply(to_decimal_days)
df['business_duration_dhm'] = df[minutes_column].apply(to_dhm_format)

df.to_csv(output_csv, index=False)
print(f"✅ Converted and saved to: {output_csv}")
