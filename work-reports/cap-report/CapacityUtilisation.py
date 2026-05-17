import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('C:\\Users\\469991\\MTN Group\\TES Solutions Architects - Documents\\General\\Reporting\\SA-Stats\\bespoke-tracker-2oct.csv')

# Example: Set hours per project category (adjust as needed)
category_hours = {
    'Type 3+ Private Network': 2,
    'CSS Feasibility': 1,
    'Type 3+' : 4,
    'Type 3+ Dark Fibre Data Centre': 4,
    'CSS Feasibility Bulk': 3,
    'Type 3+ SDWAN Cloud Campus': 3,
    'TFLS Project': 4,
    'Type 3+ LEO': 2,
    'Type 3+ DC Hosting': 4,
    'Type 3+ High Capacity': 2,
    'Type 3+ 3P Broadband': 1,
    'Type 3+ NLD Fibre MOFN': 4,
    'DeliveryTransition': 1

    # Add more categories as needed
}

# Ensure dates are datetime objects
df['Start date'] = pd.to_datetime(df['Start date'])
df['Completed Date'] = pd.to_datetime(df['Completed Date'], errors='coerce')

# Fill blank end dates with today's date (task still in progress)
today = pd.Timestamp(datetime.today())
df['Completed Date'] = df['Completed Date'].fillna(today)

# Assign fixed duration based on category (in minutes)
df['fixed_duration'] = df['Category'].map(category_hours).fillna(0) * 60  # convert hours to minutes

# If you want to use fixed duration instead of calculated duration, comment the next line
df['duration'] = (df['Completed Date'] - df['Start date']).dt.total_seconds() / 60

# Use fixed_duration for calculations (replace 'duration' with 'fixed_duration' below if desired)
use_fixed = True  # Set to False to use calculated duration

# Filter for active projects based on Progress column
active_df = df[df['Progress'] == 'In progress']

daily_rows = []

for _, row in active_df.iterrows():
    start = row['Start date']
    end = row['Completed Date']

    if pd.isnull(start) or pd.isnull(end):
        continue

    start_date = start.date()
    end_date = end.date()
    days_open = (end_date - start_date).days + 1
    if days_open <= 0:
        days_open = 1

    duration_value = row['fixed_duration'] if use_fixed else row['duration']
    duration_per_day = duration_value  # fixed hours per day, not spread

    # Daily
    for i in range(days_open):
        day = start_date + timedelta(days=i)
        daily_rows.append({
            'Assigned to': row['Assigned to'],
            'day': day,
            'duration_per_day': duration_per_day
        })

# Create DataFrame
daily_df = pd.DataFrame(daily_rows)

# Capacity in minutes
DAILY_CAPACITY = 8 * 60
WEEKLY_CAPACITY = 5 * DAILY_CAPACITY
MONTHLY_CAPACITY = 20 * DAILY_CAPACITY

# Per day
daily = daily_df.groupby(['Assigned to', 'day'])['duration_per_day'].sum().reset_index()
daily['capacity_utilisation_%'] = (daily['duration_per_day'] / DAILY_CAPACITY) * 100

# Weekly and monthly aggregation from daily_df
daily_df['week'] = pd.to_datetime(daily_df['day']).dt.isocalendar().week
daily_df['month'] = pd.to_datetime(daily_df['day']).dt.month

weekly = daily_df.groupby(['Assigned to', 'week'])['duration_per_day'].sum().reset_index()
weekly['capacity_utilisation_%'] = (weekly['duration_per_day'] / WEEKLY_CAPACITY) * 100

monthly = daily_df.groupby(['Assigned to', 'month'])['duration_per_day'].sum().reset_index()
monthly['capacity_utilisation_%'] = (monthly['duration_per_day'] / MONTHLY_CAPACITY) * 100

print("Daily Capacity Utilisation (%):")
print(daily)

print("\nWeekly Capacity Utilisation (%):")
print(weekly)

print("\nMonthly Capacity Utilisation (%):")
print(monthly)

##
def plot_utilisation(df, x_col, y_col, group_col, title, xlabel, ylabel):
    plt.figure(figsize=(12, 6))
    for key, grp in df.groupby(group_col):
        plt.plot(grp[x_col], grp[y_col], marker='o', label=str(key))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(title=group_col)
    plt.tight_layout()
    plt.show()

# # Plot daily utilisation
# plot_utilisation(
#     daily,
#     x_col='day',
#     y_col='capacity_utilisation_%',
#     group_col='Assigned to',
#     title='Daily Capacity Utilisation (%)',
#     xlabel='Day',
#     ylabel='Utilisation (%)'
# )

# # Plot weekly utilisation
# plot_utilisation(
#     weekly,
#     x_col='week',
#     y_col='capacity_utilisation_%',
#     group_col='Assigned to',
#     title='Weekly Capacity Utilisation (%)',
#     xlabel='Week',
#     ylabel='Utilisation (%)'
# )

# # Plot monthly utilisation
# plot_utilisation(
#     monthly,
#     x_col='month',
#     y_col='capacity_utilisation_%',
#     group_col='Assigned to',
#     title='Monthly Capacity Utilisation (%)',
#     xlabel='Month',
#     ylabel='Utilisation (%)'
# )

def plot_bar_utilisation(df, x_col, y_col, group_col, title, xlabel, ylabel):
    plt.figure(figsize=(14, 7))
    groups = df[group_col].unique()
    x_vals = sorted(df[x_col].unique())
    bar_width = 0.8 / len(groups)  # Adjust bar width for multiple resources

    for i, key in enumerate(groups):
        grp = df[df[group_col] == key]
        # Align bars for each resource side by side
        plt.bar(
            [x + i * bar_width for x in range(len(x_vals))],
            grp.set_index(x_col).reindex(x_vals)[y_col].fillna(0),
            width=bar_width,
            label=str(key)
        )

    plt.xticks([x + bar_width * (len(groups) - 1) / 2 for x in range(len(x_vals))], x_vals, rotation=45)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(title=group_col)
    plt.tight_layout()
    plt.show()

# Plot daily utilisation as bar chart
plot_bar_utilisation(
    daily,
    x_col='day',
    y_col='capacity_utilisation_%',
    group_col='Assigned to',
    title='Daily Capacity Utilisation (%)',
    xlabel='Day',
    ylabel='Utilisation (%)'
)

# Plot weekly utilisation as bar chart
plot_bar_utilisation(
    weekly,
    x_col='week',
    y_col='capacity_utilisation_%',
    group_col='Assigned to',
    title='Weekly Capacity Utilisation (%)',
    xlabel='Week',
    ylabel='Utilisation (%)'
)

# Plot monthly utilisation as bar chart
plot_bar_utilisation(
    monthly,
    x_col='month',
    y_col='capacity_utilisation_%',
    group_col='Assigned to',
    title='Monthly Capacity Utilisation (%)',
    xlabel='Month',
    ylabel='Utilisation (%)'
)