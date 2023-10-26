# Import the Values class from values_insert.py
from values_insert import Values

# Define a list of table names you want to insert data into
table_names = ['matches', 'deliveries', 'umpires']

# Loop through each table name
for i in range(len(table_names)):
    # Create the file path for the CSV data file for the current table
    filepath = f"/home/aviral/Desktop/projects/IPL DataSet Analytics/archive/{table_names[i]}.csv"

    # Create an instance of the Values class with the file path and table name
    obj = Values(filepath, table_names[i])

    # Call the insert_values_from_csv method to insert data into the table
    obj.insert_values_from_csv()

    print('Success!!!, Values Inserted')
