import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- CONFIGURATION ---
INPUT_FILE = 'C:\\Users\\469991\\MTN Group\\TES Solutions Architects - Documents\\General\\Reporting\\SA-Stats\\SA-Stats-2026-feb17.csv'  # Ensure this matches your filename
OUTPUT_CSV = 'C:\\Users\\469991\\MTN Group\\TES Solutions Architects - Documents\\General\\Reporting\\SA-Stats\\Weekly_Utilization_Report.csv'
HEATMAP_IMAGE = 'C:\\Users\\469991\\MTN Group\\TES Solutions Architects - Documents\\General\\Reporting\\SA-Stats\\Capacity_Heatmap.png'

def process_utilization():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: Could not find {INPUT_FILE}")
        return

    print("Loading data...")
    # 1. Load the data
    df = pd.read_csv(INPUT_FILE)

    # 2. Clean Dates (Handling the YYYY/MM/DD format)
    df['Start Date'] = pd.to_datetime(df['Start Date'], errors='coerce')
    df['End Date'] = pd.to_datetime(df['End Date'], errors='coerce')

    # 3. Clean Utilization (Convert '20%' string to 20.0 float)
    def clean_pct(val):
        if pd.isna(val): return 0.0
        if isinstance(val, str):
            return float(val.replace('%', '').strip())
        return float(val)

    df['Util_Val'] = df['Utilisation %'].apply(clean_pct)

    # Remove rows with invalid dates
    df = df.dropna(subset=['Start Date', 'End Date'])

    # 4. The "Explosion" Logic
    # We turn each row into daily entries to handle projects that span weeks
    print("Calculating daily allocations...")
    daily_rows = []
    for _, row in df.iterrows():
        # Get all business days (Mon-Fri) between Start and End
        workdays = pd.bdate_range(start=row['Start Date'], end=row['End Date'])
        
        for day in workdays:
            daily_rows.append({
                'Architect': row['Architect'],
                'Date': day,
                'Load': row['Util_Val']
            })

    df_daily = pd.DataFrame(daily_rows)

    if df_daily.empty:
        print("No valid data found to process.")
        return

    # 5. Aggregate to Weekly (Friday ending)
    # This sums up all tasks for an architect and gets the weekly average %
    print("Generating weekly buckets...")
    weekly = df_daily.groupby(['Architect', pd.Grouper(key='Date', freq='W-FRI')])['Load'].sum() / 5
    weekly = weekly.reset_index()
    weekly.columns = ['Architect', 'Week Ending', 'Utilization %']

    # 6. Create Pivot for Heatmap
    pivot = weekly.pivot(index='Architect', columns='Week Ending', values='Utilization %').fillna(0)
    
    # Save the CSVs
    weekly.to_csv(OUTPUT_CSV, index=False)
    pivot.to_csv('C:\\Users\\469991\\MTN Group\\TES Solutions Architects - Documents\\General\\Reporting\\SA-Stats\\Pivot_Table_Report.csv')
    print(f"Success! Reports saved to {OUTPUT_CSV} and Pivot_Table_Report.csv")

    # 7. Generate Heatmap
    plt.figure(figsize=(14, 7))
    # Convert dates to strings for better labels
    plot_data = pivot.copy()
    plot_data.columns = [c.strftime('%b %d') for c in plot_data.columns]
    
    sns.heatmap(plot_data, annot=True, fmt=".0f", cmap="YlOrRd", cbar_kws={'label': 'Total Load %'})
    plt.title('Team Weekly Capacity Utilization (100% = Full Capacity)')
    plt.tight_layout()
    plt.savefig(HEATMAP_IMAGE)
    print(f"Heatmap saved to {HEATMAP_IMAGE}")

if __name__ == "__main__":
    process_utilization()