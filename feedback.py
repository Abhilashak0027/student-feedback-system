def generate_feedback(marks):
    if marks < 40:
        return "Needs Improvement"
    elif marks < 70:
        return "Good effort"
    else:
        return "Excellent work"

def assign_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 75:
        return 'B'
    elif marks >= 60:
        return 'C'
    elif marks >= 40:
        return 'D'
    else:
        return 'F'
