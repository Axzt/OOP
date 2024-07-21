from main import *

run_cases = [
    (Hero("Hercules", 200), Archer("Pericles", 100, 2), 190),
    (Hero("Aquiles", 150), Archer("Aneas", 80, 1), 140),
]

submit_cases = run_cases + [
    (Hero("Paris", 120), Archer("Hector", 100, 0), None, "not enough arrows"),
    (Hero("Helen", 100), Archer("Menelaus", 50, 2), 90),
    (Hero("Odysseus", 90), Archer("Circe", 70, 1), 80),
    (Hero("Icarus", 60), Archer("Daedalus", 40, 2), 40, None, True),
    (Hero("Zeus", 1000), Archer("Hades", 900, 1), None, "not enough arrows", True),
]


def test(hero, archer, expected_result, expected_err=None, twice=False):
    print("---------------------------------")
    print(f"Hero: {hero.get_name()} with health: {hero.get_health()}")
    print(f"Archer: {archer.get_name()} with health: {archer.get_health()}")
    try:
        archer.shoot(hero)
        if twice:
            print("Shooting twice!")
            archer.shoot(hero)
        result = hero.get_health()

        if expected_err:
            print(f"Expected Exception: {expected_err}")
            print("Actual: no exception raised")
            print("Fail")
            return False

        print(f"Expecting Hero's health after shoot: {expected_result}")
        print(f"Actual: {result}")
        if result == expected_result:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print(f"Expected Exception: {expected_err}")
        print(f"Actual Exception: {e}")
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
