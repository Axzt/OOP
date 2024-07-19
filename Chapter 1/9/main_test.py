from main import *

run_cases = [(Wall(), [50, 100]), (Wall(), [50, 100, 200])]

submit_cases = run_cases + [
    (Wall(), [50, 100, 200, 400, 800]),
    (Wall(), [50, 100, 200, 400, 800, 1600]),
    (Wall(), [50, 100, 200, 400, 800, 1600, 3200]),
]


def test(wall, expected_outputs):
    print("---------------------------------")
    actual_outputs = []
    for _ in expected_outputs:
        cost = wall.get_cost()
        actual_outputs.append(cost)
        print(f"Cost of wall: {cost}")
        wall.fortify()
        print("fortifying wall...")
    print(f"Expecting: {expected_outputs}")
    print(f"Actual: {actual_outputs}")

    if actual_outputs == expected_outputs:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for wall, expected_outputs in test_cases:
        correct = test(wall, expected_outputs)
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
