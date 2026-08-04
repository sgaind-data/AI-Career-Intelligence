from queries import (
    preview_occupations,
    count_records,
    search_occupations,
    list_tables
)

LINE = "=" * 60


def print_database_summary():
    """
    Displays database statistics.
    """

    occupation_count = count_records("occupation_data")
    knowledge_count = count_records("knowledge")
    skills_count = count_records("essential_skills")
    activities_count = count_records("work_activities")
    abilities_count = count_records("abilities")
    table_count = len(list_tables())

    print("\n" + LINE)
    print("🚀 AI CAREER INTELLIGENCE PLATFORM")
    print(LINE)

    print("\n📊 DATABASE SUMMARY\n")

    print(f"📁 Total Database Tables : {table_count}")
    print(f"💼 Total Occupations     : {occupation_count.iloc[0,0]}")
    print(f"📚 Knowledge Records     : {knowledge_count.iloc[0,0]}")
    print(f"🛠️ Essential Skills      : {skills_count.iloc[0,0]}")
    print(f"⚙️ Work Activities       : {activities_count.iloc[0,0]}")
    print(f"🧠 Abilities             : {abilities_count.iloc[0,0]}")


def print_occupation_preview():
    """
    Displays the first 10 occupations.
    """

    print("\n" + LINE)
    print("🏢 TOP 10 OCCUPATIONS")
    print(LINE)

    print(preview_occupations().to_string(index=False))


def print_engineering_occupations():
    """
    Displays engineering occupations.
    """

    print("\n" + LINE)
    print("⚙️ ENGINEERING OCCUPATIONS")
    print(LINE)

    print(search_occupations("Engineer").to_string(index=False))


def print_scientist_occupations():
    """
    Displays scientist occupations.
    """

    print("\n" + LINE)
    print("🔬 SCIENTIST OCCUPATIONS")
    print(LINE)

    print(search_occupations("Scientist").to_string(index=False))


def run_dashboard():
    """
    Runs the analytics dashboard.
    """

    print_database_summary()
    print_occupation_preview()
    print_engineering_occupations()
    print_scientist_occupations()

    print("\n" + LINE)
    print("✅ Analytics Dashboard Loaded Successfully")
    print(LINE)