import os
import pandas as pd

from config import RAW_DATA_PATH


def get_csv_files():
    """
    Returns a list of all CSV files inside the raw data folder.
    """

    csv_files = []

    for file in os.listdir(RAW_DATA_PATH):
        if file.endswith(".csv"):
            csv_files.append(file)

    return csv_files


def load_csv(file_name):
    """
    Loads a CSV file from the raw data folder.
    """

    file_path = os.path.join(RAW_DATA_PATH, file_name)

    dataframe = pd.read_csv(file_path)

    return dataframe