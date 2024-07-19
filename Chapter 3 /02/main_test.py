from main import *

run_cases = [
    ((0, 0, 5, 3), ["sprint_right"], (10, 0)),
    (
        (0, 0, 20, 3),
        [
            "sprint_left",
            "sprint_left",
            "sprint_left",
        ],
        (-120, 0),
    ),
    ((1, 1, 3, 1), ["sprint_down", "sprint_right"], "not enough stamina to sprint"),
]

submit_cases = run_cases + [
    ((3, 5, 5, 1), ["sprint_up"], (3, 15)),
    ((2, 15, 6, 2), ["sprint_down"], (2, 3)),
    (
        (1, 1, 5, 2),
        ["sprint_left", "sprint_up", "sprint_down"],
        "not enough stamina to sprint",
    ),
]


def test(human_args, methods, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    human = Human(*human_args)
    print(
        f" * human: x pos: {human._Human__pos_x}, y pos: {human._Human__pos_y}, speed: {human._Human__speed}, stamina: {human._Human__stamina}"
    )
    print(f" * methods: {methods}")
    print(f"Expected: {expected_output}")
    try:
        for method in methods:
            getattr(human, method)()
        result = human.get_position()
    except Exception as e:
        result = str(e)
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
