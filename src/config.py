import os

# Base project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Data folders
DATA_PATH = os.path.join(BASE_DIR, "data")
RAW_DATA_PATH = os.path.join(DATA_PATH, "raw")
DATABASE_PATH = os.path.join(DATA_PATH, "database")

# Output folder
OUTPUT_PATH = os.path.join(BASE_DIR, "reports")

# Database file
DATABASE_FILE = os.path.join(
    DATABASE_PATH,
    "career_intelligence.db"
)