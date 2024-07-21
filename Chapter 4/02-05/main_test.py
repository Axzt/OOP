from main import *

run_cases = [
    ("Will the Archer", 1, "Darren the Crossbowman", 4, None, 1),
    ("Elena the Archer", 5, "Connor the Crossbowman", 3, None, 0),
    ("Lara the Archer", 3, "Marcus the Crossbowman", 2, "not enough arrows", -1),
    ("Jake the Archer", 0, "Victor the Crossbowman", 3, None, 0),
]

submit_cases = run_cases + [
    ("Sophia the Archer", 7, "Oscar the Crossbowman", 5, None, 2),
    ("Ryan the Archer", 2, "Emma the Crossbowman", 1, "not enough arrows", None),
    ("Zoe the Archer", 10, "Lucas the Crossbowman", 8, None, 5),
    ("Isaac the Archer", 4, "Hannah the Crossbowman", 0, "not enough arrows", None),
]


def test(
    archer_name,
    archer_arrows,
    crossbowman_name,
    crossbowman_bolts,
    expected_exception,
    expected_remaining_bolts,
):
    print("---------------------------------")
    print(f"Creating an archer named {archer_name} with {archer_arrows} arrows")
    archer = Archer(archer_name, archer_arrows)
    print(
        f"Creating a crossbowman named {crossbowman_name} with {crossbowman_bolts} bolts"
    )
    crossbowman = Crossbowman(crossbowman_name, crossbowman_bolts)
    try:
        expected_str = f"{archer_name} was shot by 3 crossbow bolts"
        actual_str = crossbowman.triple_shot(archer)
        if actual_str != expected_str:
            print("Expected: " + expected_str)
            print("Actual: " + actual_str)
            print("Fail")
            return False
        else:
            print(actual_str)
        if expected_exception:
            print(
                f"Expected exception '{expected_exception}', but no exception occurred"
            )
            print("Fail")
            return False
        elif crossbowman.get_num_arrows() != expected_remaining_bolts:
            print(
                f"Expected remaining arrows: {expected_remaining_bolts}, Actual: {crossbowman.get_num_arrows()}"
            )
            print("Fail")
            return False
        else:
            print(
                f"Expected {expected_remaining_bolts} remaining bolts, Actual: {crossbowman.get_num_arrows()}"
            )
            print("Pass")
            return True
    except Exception as e:
        if str(e) == expected_exception:
            print(f"Expected exception: {expected_exception}")
            print(f"Caught expected exception: {e}")
            print("Pass")
            return True
        else:
            print(f"Unexpected exception: {e}")
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
