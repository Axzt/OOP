from main import *

run_cases = [
    (Rectangle(0, 0, 4, 4), (0, 4, 4, 0)),
    (Rectangle(4, 4, 0, 0), (0, 4, 4, 0)),
]

submit_cases = run_cases + [
    (Rectangle(1, 2, 3, 4), (1, 3, 4, 2)),
    (Rectangle(3, 4, 1, 2), (1, 3, 4, 2)),
    (Rectangle(2, 1, 5, 4), (2, 5, 4, 1)),
    (Rectangle(5, 4, 2, 1), (2, 5, 4, 1)),
    (Rectangle(3, 3, 3, 3), (3, 3, 3, 3)),
]


def test(rectangle, expected_output):
    print("---------------------------------")
    print(f"Inputs: {rectangle}")
    print(f"Expecting: {expected_output}")
    result = (
        rectangle.get_left_x(),
        rectangle.get_right_x(),
        rectangle.get_top_y(),
        rectangle.get_bottom_y(),
    )
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
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
