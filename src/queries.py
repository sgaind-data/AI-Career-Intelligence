import pandas as pd

from database import create_database


def run_query(query):
    """
    Executes a SQL query and returns the results as a Pandas DataFrame.
    """

    connection = create_database()

    result = pd.read_sql_query(query, connection)

    connection.close()

    return result


def preview_occupations(limit=10):
    """
    Returns the first N occupations.
    """

    query = f"""
    SELECT
        `O*NET-SOC Code`,
        Title
    FROM occupation_data
    LIMIT {limit};
    """

    return run_query(query)


def count_records(table_name):
    """
    Returns the total number of records in a table.
    """

    query = f"""
    SELECT COUNT(*) AS Total
    FROM {table_name};
    """

    return run_query(query)


def search_occupations(keyword):
    """
    Searches occupations by keyword.
    """

    query = f"""
    SELECT Title
    FROM occupation_data
    WHERE Title LIKE '%{keyword}%'
    ORDER BY Title;
    """

    return run_query(query)


def list_tables():
    """
    Returns all database tables.
    """

    query = """
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    ORDER BY name;
    """

    return run_query(query)