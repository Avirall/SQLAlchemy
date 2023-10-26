from sqlalchemy_utils import drop_database

# PostgreSQL database URL (modify with your database details)
db_url = "postgresql://postgres:sample123@localhost/test_db"

# Delete the database
drop_database(db_url)
