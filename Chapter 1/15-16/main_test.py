from main import *

run_cases = [
    (
        Archer("Robin", 2, 2),
        Archer("Sheriff", 2, 2),
        1,
        [("Robin", 1, 1), ("Sheriff", 1, 1)],
        None,
    ),
    (
        Archer("Friar Tuck", 1, 0),
        Archer("Prince John", 1, 0),
        1,
        [None, None],
        "Friar Tuck can't shoot",
    ),
    (
        Archer("King Richard", 1, 1),
        Archer("Prince John", 2, 1),
        1,
        [None, None],
        "King Richard is dead",
    ),
]

submit_cases = run_cases + [
    (
        Archer("Robin", 2, 2),
        Archer("Sheriff", 3, 1),
        2,
        [None, None],
        "Sheriff can't shoot",
    ),
    (
        Archer("Marian", 3, 2),
        Archer("Little John", 3, 3),
        2,
        [("Marian", 1, 0), ("Little John", 1, 1)],
        None,
    ),
    (
        Archer("Robin", 2, 2),
        Archer("Prince John", 2, 1),
        2,
        [None, None],
        "Prince John is dead",
    ),
    (
        Archer("Little John", 4, 3),
        Archer("Sheriff", 3, 2),
        3,
        [None, None],
        "Sheriff is dead",
    ),
]


def test(archer_1, archer_2, rounds, expected_result, expected_err):
    print("---------------------------------")
    archer_1.print_status()
    archer_2.print_status()

    try:
        for _ in range(rounds):
            archer_1.shoot(archer_2)
            archer_2.print_status()
            archer_2.shoot(archer_1)
            archer_1.print_status()
        archer_2.print_status()

        if expected_err:
            print(f"\nExpected Exception: {expected_err}")
            print("Actual: no exception raised")
            print("Fail")
            return False

        status_1 = archer_1.get_status()
        status_2 = archer_2.get_status()
        print(f"\nExpected Result: {expected_result[0]}, {expected_result[1]}")
        print(f"Actual Result: {status_1}, {status_2}")

        if status_1 == expected_result[0] and status_2 == expected_result[1]:
            print("Pass")
            return True
        else:
            print("Fail")
            return False
    except Exception as e:
        print(f"\nExpected Exception: {expected_err}")
        print(f"Actual Exception: {str(e)}")
        if str(e) == expected_err:
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
