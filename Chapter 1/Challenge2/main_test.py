from main import *

run_cases = [
    [
        (
            "John",
            "Carmack",
            1,
            "Senior Developer",
            100000,
        ),
        (
            "Shigeru",
            "Miyamoto",
            2,
            "Staff Developer",
            120000,
        ),
        (
            "Ken",
            "Levine",
            1,
            "Manager",
            170000,
        ),
        (
            "Will",
            "Wright",
            2,
            "Game Developer",
            125000,
        ),
    ]
]

submit_cases = run_cases + [
    [
        (
            "Sid",
            "Meier",
            1,
            "Junior Developer",
            160000,
        ),
        (
            "Gabe",
            "Newell",
            2,
            "Staff Developer",
            130000,
        ),
        (
            "Sarah",
            "Schulte",
            3,
            "Principal Bash Developer",
            10000000,
        ),
    ]
]

expected_total_employees = 0


def test(employees):
    print("=================================")
    for employee in employees:
        global expected_total_employees
        expected_total_employees += 1
        print(
            f"Employee({employee[0]}, {employee[1]}, {employee[2]}, {employee[3]}, {employee[4]})"
        )
        employee = Employee(*employee)
        expected_name = f"{employee.first_name} {employee.last_name}"
        print(f"Expected name: {expected_name}")
        print(f"Actual name: {employee.get_name()}")
        if expected_name != employee.get_name():
            return False

        print(f"Expected employees: {expected_total_employees}")
        print(f"Actual employees: {Employee.total_employees}")
        if expected_total_employees != Employee.total_employees:
            return False
        print("---------------------------------")
    return True


def main():
    passed, failed = 0, 0
    for test_case in test_cases:
        correct = test(test_case)
        if correct:
            passed += 1
            print("Pass")
        else:
            failed += 1
            print("Fail")

    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


if "__RUN__" in globals():
    test_cases = run_cases
else:
    test_cases = submit_cases

main()
