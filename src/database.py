import os
import sqlite3
import pandas as pd

from config import DATABASE_FILE


def create_database():
    """
    Creates a connection to the SQLite database.
    """
    
    database_path = DATABASE_FILE

    connection = sqlite3.connect(database_path)
    
    print(f"Connected to database: {database_path}")
    
    return connection

def load_table(connection, dataframe, table_name):
    """
    Loads a Pandas DataFrame into a SQLite table.
    """
    
    dataframe.to_sql(
        table_name,
        connection,
        if_exists="replace",
        index=False
    )