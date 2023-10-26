from sqlalchemy_utils import create_database

# PostgreSQL database URL (modify with your database details)
db_url = "postgresql://postgres:sample123@localhost/ipl"

# Create the database
create_database(db_url)
