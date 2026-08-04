import sqlite3

from config import DATABASE_FILE


def create_database():
    """
    Creates and returns a SQLite connection.
    """

    connection = sqlite3.connect(DATABASE_FILE)

    return connection


def load_table(connection, dataframe, table_name):
    """
    Loads a DataFrame into SQLite.
    """

    dataframe.to_sql(
        table_name,
        connection,
        if_exists="replace",
        index=False
    )