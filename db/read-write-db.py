import pyodbc

# Path to your Access database file
db_file = r'C:\Users\469991\OneDrive - MTN Group\Documents\Database2.accdb'

# Connection string for Access .accdb files
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    rf'DBQ={db_file};'
)

# Connect to the database
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# 🔍 READ: Fetch all rows from a table
def read_data(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# ✍️ WRITE: Insert a new row into a table
def insert_data(table_name, columns, values):
    placeholders = ', '.join(['?'] * len(values))
    sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
    cursor.execute(sql, values)
    conn.commit()
    print("Data inserted successfully.")

# Example usage
if __name__ == "__main__":
    table ='Table1'  # Replace with your table name

    print("Reading data:")
    read_data(table)

    print("\nInserting new data:")
    insert_data(table, ['Field1', 'Field2', 'Field3'], ['Alice', 'Smith', 30])

    print("\nUpdated data:")
    read_data(table)

# Close the connection
cursor.close()
conn.close()