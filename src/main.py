import os
import pandas as pd

from config import OUTPUT_PATH
from loader import get_csv_files, load_csv
from profiler import profile_dataframe, profile_columns
from database import create_database, load_table
from analytics import run_dashboard


def main():
    """
    Main application workflow.
    """

    # -------------------------------------------------
    # Connect to SQLite database
    # -------------------------------------------------

    connection = create_database()

    # -------------------------------------------------
    # Discover CSV files
    # -------------------------------------------------

    csv_files = get_csv_files()

    all_profiles = []
    all_column_profiles = []

    # -------------------------------------------------
    # Process every dataset
    # -------------------------------------------------

    for file in csv_files:

        dataframe = load_csv(file)

        table_name = os.path.splitext(file)[0]

        load_table(
            connection,
            dataframe,
            table_name
        )

        profile = profile_dataframe(
            dataframe,
            file
        )

        all_profiles.append(profile)

        column_profiles = profile_columns(
            dataframe,
            file
        )

        all_column_profiles.extend(column_profiles)

    # -------------------------------------------------
    # Save profile summary
    # -------------------------------------------------

    summary_df = pd.DataFrame(all_profiles)

    os.makedirs(OUTPUT_PATH, exist_ok=True)

    summary_df.to_csv(
        os.path.join(OUTPUT_PATH, "profile_summary.csv"),
        index=False
    )

    # -------------------------------------------------
    # Save column profile
    # -------------------------------------------------

    column_df = pd.DataFrame(all_column_profiles)

    column_df.to_csv(
        os.path.join(OUTPUT_PATH, "column_profile.csv"),
        index=False
    )

    print("\n✅ Profile Summary Created")
    print("📄 outputs/profile_summary.csv")

    print("\n✅ Column Profile Created")
    print("📄 outputs/column_profile.csv")

    # -------------------------------------------------
    # Close ETL connection
    # -------------------------------------------------

    connection.close()

    print("\n✅ Database connection closed.")

    # -------------------------------------------------
    # Launch analytics dashboard
    # -------------------------------------------------

    run_dashboard()


if __name__ == "__main__":
    main()