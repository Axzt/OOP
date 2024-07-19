from main import *

run_cases = [
    (
        "Zatanna",
        ["Maths", "Lore", "History"],
        [85, 92, 76],
        {"Maths": "B", "Lore": "A", "History": "C"},
    ),
    (
        "Prospero",
        ["Alchemy", "Politics"],
        [90, 88],
        {"Alchemy": "A", "Politics": "B"},
    ),
]

submit_cases = run_cases + [
    (
        "Glinda",
        ["Elementalism", "Artificery", "History"],
        [80, 79, 90],
        {"Elementalism": "B", "Artificery": "C", "History": "A"},
    ),
    (
        "Willow",
        ["Treasure Hunting", "Artificery"],
        [70, 65],
        {"Treasure Hunting": "C", "Artificery": "D"},
    ),
    (
        "Rincewind",
        ["Necromancy"],
        [100],
        {"Necromancy": "A"},
    ),
]


def test(name, courses, scores, expected_grades):
    print("---------------------------------")
    student = Student(name)
    for i in range(len(courses)):
        student.add_course(courses[i], scores[i])
    actual_grades = student.get_courses()

    print(f"Inputs for {name}:")
    print(f" * Courses: {courses}")
    print(f" * Scores: {scores}")
    print(f" * Expected Grades: {expected_grades}")
    print(f" * Actual Grades: {actual_grades}")

    if actual_grades == expected_grades:
        print("Pass")
        return True
    else:
        print("Fail")
        return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
