import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file
df = pd.read_csv('C:\\Users\\469991\\MTN Group\\TES Solutions Architects - Documents\\General\\Reporting\\Feasibility\\OLA-2025\\2025-monthly\\oct-manual-volumes.csv', parse_dates=['AUDIT_DAY'])

# Truncate time to date only
df['DATE_ONLY'] = df['AUDIT_DAY'].dt.date

# Pivot the data: rows = date, columns = assigned_to, values = record_count
pivot = df.pivot_table(index='DATE_ONLY', columns='ASSIGNED_TO', values='RECORD_COUNT', aggfunc='sum').fillna(0)

# Plot grouped bar chart
pivot.plot(kind='bar', figsize=(12, 6))
plt.title('Manual Audit Counts per Day by Assigned Region')
plt.xlabel('Audit Date')
plt.ylabel('Record Count')
plt.xticks(rotation=45)
plt.legend(title='Assigned To', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
