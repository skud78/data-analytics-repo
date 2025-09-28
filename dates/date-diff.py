import pandas as pd
from datetime import datetime
import holidays

# Load your CSV
df = pd.read_csv(r'C:\Users\469991\MTN Group\TES Solutions Architects - Documents\General\Reporting\Feasibility\OLA-2025\sample-output-audit-data\CSS-aug-result.csv', parse_dates=['start_date', 'end_date'])

# Define South African holidays
za_holidays = holidays.SouthAfrica()



from datetime import timedelta


# Function Business Time Breakdown
def business_time_breakdown(start, end):
    if pd.isnull(start) or pd.isnull(end):
        return None
    # Generate all days in range
    all_days = pd.date_range(start, end, freq='D')
    # Filter out weekends and holidays
    business_days = [day for day in all_days if day.weekday() < 5 and day not in za_holidays]
    
    # Total seconds between start and end
    total_seconds = 0
    for day in business_days:
        # If start and end are on the same day
        if day.date() == start.date() == end.date():
            total_seconds += (end - start).total_seconds()
        elif day.date() == start.date():
            total_seconds += (datetime.combine(day, datetime.max.time()) - start).total_seconds()
        elif day.date() == end.date():
            total_seconds += (end - datetime.combine(day, datetime.min.time())).total_seconds()
        else:
            total_seconds += 86400  # full business day

    # Convert seconds to days, hours, minutes
    td = timedelta(seconds=total_seconds)
    days = td.days
    hours, remainder = divmod(td.seconds, 3600)
    minutes = remainder // 60
    return f"{days}d {hours}h {minutes}m"

def business_minutes_excl_holidays(start, end):
    if pd.isnull(start) or pd.isnull(end):
        return None
    # Generate date range
    all_days = pd.date_range(start, end, freq='D')
    # Filter out weekends and holidays
    business_days = [day for day in all_days if day.weekday() < 5 and day not in za_holidays]
    
    total_minutes = 0
    for day in business_days:
        # If start and end are on the same day
        if day.date() == start.date() == end.date():
            total_minutes += (end - start).total_seconds() / 60
        elif day.date() == start.date():
            total_minutes += (datetime.combine(day, datetime.max.time()) - start).total_seconds() / 60
        elif day.date() == end.date():
            total_minutes += (end - datetime.combine(day, datetime.min.time())).total_seconds() / 60
        else:
            total_minutes += 1440  # full day in minutes

    return round(total_minutes)

# Function to count business days
def business_days_excl_holidays(start, end):
    if pd.isnull(start) or pd.isnull(end):
        return None
    # Generate date range
    all_days = pd.date_range(start, end, freq='D')
    # Filter out weekends and holidays
    business_days = [day for day in all_days if day.weekday() < 5 and day not in za_holidays]
    return len(business_days)

# Apply function row-wise
# df['business_days'] = df.apply(lambda row: business_days_excl_holidays(row['start_date'], row['end_date']), axis=1)
#df['business_duration'] = df.apply(lambda row: business_time_breakdown(row['start_date'], row['end_date']), axis=1)
# df[['bd_days', 'bd_hours', 'bd_minutes']] = df['business_duration'].str.extract(r'(\d+)d (\d+)h (\d+)m').astype(float)
df['business_minutes'] = df.apply(lambda row: business_minutes_excl_holidays(row['start_date'], row['end_date']), axis=1)
df['business_days_decimal'] = df['business_minutes'] / 1440


#Python Function: Convert Minutes to Xd Yh Zm
def format_minutes_to_dhm(minutes):
    if pd.isnull(minutes):
        return None
    total_minutes = int(minutes)
    days = total_minutes // 1440
    remainder = total_minutes % 1440
    hours = remainder // 60
    mins = remainder % 60
    return f"{days}d {hours}h {mins}m"

df['business_duration_dhm'] = df['business_minutes'].apply(format_minutes_to_dhm)


# Ensure the column is numeric
df['business_days_decimal'] = pd.to_numeric(df['business_days_decimal'], errors='coerce')

# Export without quotes around numbers
df.to_csv(r'C:\Users\469991\MTN Group\TES Solutions Architects - Documents\General\Reporting\Feasibility\OLA-2025\sample-output-audit-data\business_days_output.csv', index=False, float_format='%.2f')
