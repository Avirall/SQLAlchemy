import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schemas import Base, Deliveries,Match,Umpire   
# Import the necessary SQLAlchemy classes from your schemas.py

# Define the SQLAlchemy engine and session
engine = create_engine("postgresql://postgres:sample123@localhost:5432/ipl", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# This class recieves file path of the csv and the table name in which we want to insert the data
class Values:
    filepath = ''
    table_name = ''

    
    def __init__(self, filepath, table_name):
        self.filepath = filepath
        self.table_name = table_name
    
    # This function extracts column names from the table and returns it as a list
    def get_column_names_by_table(self):
        table = Base.metadata.tables.get(self.table_name)
        if table is not None:
            return [column.name for column in table.columns]
        else:
            return []
        
    # This fucntion puts values while looping through the list name and reading csv lines one by one
    def insert_values_from_csv(self):
        column_names = self.get_column_names_by_table()
        column_names=column_names[1:]
        with open(self.filepath, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data = {column: row[column] for column in column_names}

                if self.table_name == 'deliveries':
                    new_record = Deliveries(**data)
                    session.add(new_record)
                elif self.table_name == 'matches':
                    new_record = Match(**data)
                    session.add(new_record)
                elif self.table_name == 'umpires':
                    new_record = Umpire(**data)
                    session.add(new_record)
                else:
                    print(f"Table '{self.table_name}' not found.")
                    return

        session.commit()
