from database import create_table, insert_student, get_all_students
from feedback import generate_feedback, assign_grade
from analytics import export_report_to_csv

# Step 1: Create table
create_table()

# Step 2: Insert sample data
insert_student("Abhilasha", 101, "Math", 85)
insert_student("Abhilasha", 101, "Science", 62)
insert_student("Abhilasha", 101, "English", 33)
insert_student("Komal", 102, "Math", 95)
insert_student("Komal", 102, "Science", 78)

# Step 3: Show feedback and grade
print("\n🎓 Student Performance Report:")
students = get_all_students()
for student in students:
    name, roll_no, subject, marks = student
    feedback = generate_feedback(marks)
    grade = assign_grade(marks)
    print(f"{name} | Roll No: {roll_no} | Subject: {subject} | Marks: {marks} | Grade: {grade} | Feedback: {feedback}")

# Step 4: Export report
export_report_to_csv()
