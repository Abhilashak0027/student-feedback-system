import sqlite3
import pandas as pd

def export_report_to_csv():
    conn = sqlite3.connect('student_data.db')
    df = pd.read_sql_query("SELECT * FROM students", conn)
    avg_df = df.groupby(['name', 'roll_no'])['marks'].mean().reset_index()
    avg_df.rename(columns={'marks': 'average_marks'}, inplace=True)
    report = pd.merge(df, avg_df, on=['name', 'roll_no'])
    report.to_csv('student_report.csv', index=False)
    conn.close()
    print("✅ Report exported to student_report.csv")
