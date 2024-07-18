from main import *

run_cases = [(Wall, 10, 5)]

submit_cases = run_cases + [
    (Wall, 10, 5),
    (Wall, 10, 5),
    (Wall, 10, 5),
    (Wall, 10, 5),
    (Wall, 10, 5),
    (Wall, 10, 5),
]


def test(class_instance, expected_armor, expected_height):
    print("---------------------------------")
    print(f"Inputs: {class_instance}, {expected_armor}, {expected_height}")
    try:
        instance = class_instance()
        actual_armor = instance.armor
        actual_height = instance.height
        print(f"Expecting: armor={expected_armor}, height={expected_height}")
        print(f"Actual: armor={actual_armor}, height={actual_height}")
        if actual_armor == expected_armor and actual_height == expected_height:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print(f"Error: {e}")
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
