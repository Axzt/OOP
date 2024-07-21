from main import *

run_cases = [
    (Rectangle(0, 0, 4, 4), "corner1: (0,0) corner2: (4,4)"),
    (Rectangle(4, 4, 0, 0), "corner1: (4,4) corner2: (0,0)"),
]

submit_cases = run_cases + [
    (Rectangle(2, -2, 3, 4), "corner1: (2,-2) corner2: (3,4)"),
    (Rectangle(-1, -1, 1, 1), "corner1: (-1,-1) corner2: (1,1)"),
    (Rectangle(5, 5, 10, 10), "corner1: (5,5) corner2: (10,10)"),
    (Rectangle(-10, -10, -5, -5), "corner1: (-10,-10) corner2: (-5,-5)"),
]


def describe(rectangle):
    return f"corner1: ({rectangle.x1},{rectangle.y1}) corner2: ({rectangle.x2},{rectangle.y2})"


def test(rectangle, expected_output):
    try:
        print("---------------------------------")
        print(f"Inputs:")
        print(
            f" * rectangle corners: {rectangle.x1}, {rectangle.y1}, {rectangle.x2}, {rectangle.y2}"
        )
        print(f"Expecting: {expected_output}")
        result = describe(rectangle)
        print(f"Actual: {result}")
        if result == expected_output:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print(f"Error: {e}")
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
