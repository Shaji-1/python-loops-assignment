# Name: MOHAMED SHAJITH J
# Roll Number: 2602040
# Assignment: Python - Functions & Modularity
def process_scores(students):
    averages = {}
    for name, marks in students.items():
        average = sum(marks) / len(marks)
        averages[name] = round(average, 2)
    return averages
def classify_grades(averages):
    # Thresholds inside function (as requested)
    a_cutoff = 90
    b_cutoff = 75
    c_cutoff = 60
    result = {}
    for name, avg in averages.items():
        if avg >= a_cutoff:
            grade = "A"
        elif avg >= b_cutoff:
            grade = "B"
        elif avg >= c_cutoff:
            grade = "C"
        else:
            grade = "F"
        result[name] = (avg, grade)
    return result
def generate_report(classified, passing_avg=70):
    total_students = len(classified)
    passed = 0
    print("===== Student Grade Report =====")
    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"
        if status == "PASS":
            passed += 1
        print(f"{name:<8} | Avg: {avg:>5.2f} | Grade: {grade} | Status: {status}")
    failed = total_students - passed
    print("===============================")
    print()
    print(f"Total Students : {total_students}")
    print(f"Passed         : {passed}")
    print(f"Failed         : {failed}")
    return passed

if __name__ == "__main__":
    students_data = {
        "Alice": [85, 88, 86],
        "Bob": [60, 65, 62, 63],
        "Clara": [95, 97, 96, 97]
    }
    averages = process_scores(students_data)
    classified = classify_grades(averages)
    generate_report(classified)
