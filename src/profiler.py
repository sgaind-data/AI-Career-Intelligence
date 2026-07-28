import pandas as pd

def profile_dataframe(dataframe, file_name):
    """
    Returns basic profiling information about a DataFrame.
    """

    profile = {
        "File Name": file_name,
        "Rows": dataframe.shape[0],
        "Columns": dataframe.shape[1],
        "Missing Values": int(dataframe.isnull().sum().sum()),
        "Duplicate Rows": int(dataframe.duplicated().sum()),
        "Memory (MB)": round(
            dataframe.memory_usage(deep=True).sum() / (1024 * 1024), 2
        ),
    }

    return profile

def profile_columns(dataframe, file_name):
    """
    Returns profiling information for every column in a DataFrame.
    """

    column_profiles = []

    for column in dataframe.columns:

        profile = {
            "File Name": file_name,
            "Column Name": column,
            "Data Type": str(dataframe[column].dtype),
            "Missing Values": int(dataframe[column].isnull().sum()),
            "Missing %": round(
                (dataframe[column].isnull().sum() / len(dataframe)) * 100,
                2
            ),
            "Unique Values": int(dataframe[column].nunique()),
            "Sample Value": str(dataframe[column].dropna().iloc[0])
            if dataframe[column].dropna().shape[0] > 0
            else "No Data"
        }

        column_profiles.append(profile)

    return column_profiles