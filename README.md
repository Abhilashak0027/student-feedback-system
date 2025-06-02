# 🎓 Student Performance Tracker
A Python + SQLite-based application to track student marks, generate performance feedback, assign grades, and export reports.
---
##  Features
- Add and store student data in an SQLite database
- Automatically assign feedback and grades based on marks
- Generate performance reports in the terminal
- Export a detailed CSV report for further analysis or visualization
---
##  Technologies Used
- Python 3.12
- SQLite (via built-in `sqlite3`)
- Pandas (for CSV export)
---
##  Project Structure
├── main.py # Main script to run the tracker
├── database.py # Handles database operations
├── feedback.py # Feedback and grading logic
├── analytics.py # Reporting and CSV export
├── student_data.db # SQLite database file (auto-created)
├── student_report.cs # Exported performance report
