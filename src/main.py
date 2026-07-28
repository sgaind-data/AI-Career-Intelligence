import os
import pandas as pd

from config import OUTPUT_PATH
from loader import get_csv_files, load_csv
from profiler import profile_dataframe, profile_columns

if __name__ == "__main__":

    # Step 1: Get all CSV files
    csv_files = get_csv_files()

    # Store file-level profiles
    all_profiles = []

    # Store column-level profiles
    all_column_profiles = []

    # Step 2: Process every CSV
    for file in csv_files:

        dataframe = load_csv(file)

        # File-level profile
        profile = profile_dataframe(dataframe, file)
        all_profiles.append(profile)

        # Column-level profile
        column_profiles = profile_columns(dataframe, file)
        all_column_profiles.extend(column_profiles)

    # -----------------------------
    # Create summary report
    # -----------------------------
    summary_df = pd.DataFrame(all_profiles)

    os.makedirs("outputs", exist_ok=True)

    summary_df.to_csv(
        "outputs/profile_summary.csv",
        index=False
    )

    # -----------------------------
    # Create column profile report
    # -----------------------------
    column_df = pd.DataFrame(all_column_profiles)

    column_df.to_csv(
        "outputs/column_profile.csv",
        index=False
    )

    print("\n✅ Profile Summary Created")
    print("📄 outputs/profile_summary.csv")

    print("\n✅ Column Profile Created")
    print("📄 outputs/column_profile.csv")