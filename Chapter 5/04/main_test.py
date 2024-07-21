from main import *

run_cases = [
    (Dragon("Green Dragon", -1, -2, 1, 2, 1), -2, -3, 0, 0, True),
    (Dragon("Red Dragon", 2, 2, 2, 2, 2), 0, 1, 1, 0, True),
    (Dragon("Blue Dragon", 4, -3, 2, 1, 1), -5, -5, 5, 5, True),
    (Dragon("Silver Dragon", 0, 0, 5, 5, 10), 4, 0, 5, 1, False),
]

submit_cases = run_cases + [
    (Dragon("Green Dragon", -1, -2, 1, 2, 1), -3, -3, -1, -1, True),
    (Dragon("Red Dragon", 2, 2, 2, 2, 2), 5, 5, 10, 10, False),
    (Dragon("Blue Dragon", 4, -3, 2, 1, 1), 0, 0, 10, 10, False),
    (Dragon("Black Dragon", 5, -1, 3, 2, 2), -10, -10, 10, 10, True),
    (Dragon("White Dragon", 0, 0, 1, 1, 1), -1, -1, 1, 1, True),
]


def test(dragon, input1, input2, input3, input4, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(
        f" * Dragon position and size: {dragon.pos_x}, {dragon.pos_y}, {dragon.height}, {dragon.width}"
    )
    print(f" * Area corners: ({input1}, {input2}), ({input3}, {input4})")
    print(f"Expected in area: {expected_output}")
    result = dragon.in_area(input1, input2, input3, input4)
    print(f"  Actual in area: {result}")
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
