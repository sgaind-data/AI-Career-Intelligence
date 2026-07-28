# 🚀 AI Career Intelligence Platform

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)
![SQL](https://img.shields.io/badge/SQL-Analytics-336791?logo=postgresql)
![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?logo=git)
![Build in Public](https://img.shields.io/badge/Build-In_Public-success)

![AI Career Intelligence Banner](assets/banner.png)

> Transforming 45 O*NET datasets into an AI-powered Career Intelligence Platform using Python, SQL, SQLite, Power BI, Retrieval-Augmented Generation (RAG), and Large Language Models.

---

# 📌 Project Vision

Choosing a career shouldn't require searching through hundreds of web pages.

The goal of this project is to transform the official **O*NET occupational database** into an intelligent career assistant capable of answering questions such as:

- What skills are required for a Data Scientist?
- Which occupations are most similar?
- What career path should I follow?
- Which skills should I learn next?
- What jobs best align with my interests?

Rather than jumping straight into AI, this project focuses on building a strong data foundation first. Every stage—from data profiling to database design, analytics, and AI—is being developed incrementally using software engineering best practices.

---

# 🏗 Current Architecture

```text
                  O*NET CSV Files
                         │
                         ▼
           Automated Data Profiling
                         │
                         ▼
            Column-Level Metadata
                         │
                         ▼
             SQLite Relational Database
                         │
                         ▼
                SQL Analytics Layer
                         │
                         ▼
              Power BI Dashboards
                         │
                         ▼
        AI Career Intelligence Assistant
```

---

# 📂 Project Structure

```text
AI-Career-Intelligence/
│
├── assets/
│   ├── banner.png
│   ├── profile-summary.png
│   └── column-profile.png
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── database/
│
├── outputs/
│   ├── profile_summary.csv
│   └── column_profile.csv
│
├── src/
│   ├── config.py
│   ├── loader.py
│   ├── profiler.py
│   └── main.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🚀 Project Status

| Milestone | Status |
|------------|--------|
| Project Setup | ✅ Complete |
| Modular Python Architecture | ✅ Complete |
| Automated CSV Discovery | ✅ Complete |
| File-Level Data Profiling | ✅ Complete |
| Column-Level Data Profiling | ✅ Complete |
| Missing Value Analysis | ✅ Complete |
| Duplicate Detection | ✅ Complete |
| Automated Report Generation | ✅ Complete |
| SQLite Database | 🔄 Next |
| SQL Analytics Layer | ⏳ Planned |
| Power BI Dashboards | ⏳ Planned |
| Retrieval-Augmented Generation (RAG) | ⏳ Planned |
| AI Career Intelligence Assistant | ⏳ Planned |

---

# 📊 Project Output

The following reports are generated automatically by the Python profiling pipeline developed in **Part 1**.

## File-Level Data Profiling

The pipeline analyzes every O*NET dataset and automatically generates a report containing:

- Number of rows
- Number of columns
- Missing values
- Duplicate rows
- Memory usage

![Profile Summary](assets/profile-summary.png)

---

## Column-Level Data Profiling

The pipeline also profiles every column across all datasets, reporting:

- Data type
- Missing values
- Missing percentage
- Unique values
- Sample values

![Column Profile](assets/column-profile.png)

---

# 🛠 Tech Stack

### Languages

- Python
- SQL

### Data Processing

- Pandas
- SQLite *(coming next)*

### Analytics & Visualization

- Power BI *(planned)*

### Artificial Intelligence

- Retrieval-Augmented Generation (RAG) *(planned)*
- Large Language Models *(planned)*
- FastAPI *(planned)*

### Development

- Git
- GitHub

---

# 🎯 Project Goals

This project is designed to demonstrate end-to-end AI and data engineering skills, including:

- Data Engineering
- Data Profiling
- Relational Database Design
- SQL Analytics
- Business Intelligence
- Retrieval-Augmented Generation (RAG)
- AI Application Development
- Software Engineering Best Practices

---

# 🤝 Build in Public

This repository is being developed publicly from the ground up.

Instead of showcasing only the finished product, every milestone—from raw occupational datasets to a fully functional AI Career Intelligence Platform—is documented through GitHub commits and LinkedIn project updates.

The goal is to share not only **what** was built, but also **how** it was built and the engineering decisions behind it.

If you're interested in AI, Data Science, Data Engineering, Analytics, or Software Engineering, feel free to follow the journey and share your feedback.

⭐ If you find this project interesting, consider starring the repository.