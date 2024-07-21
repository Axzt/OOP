from main import *

run_cases = [
    (
        Wizard("Harry", 30, 70),
        Archer("Pericles", 100, 3),
        ["cast", "shoot", "shoot"],
        [10, 75],
    ),
    (
        Wizard("Ron", 50, 90),
        Archer("Odysseus", 80, 2),
        ["shoot", "shoot", "shoot", "cast"],
        [None, None],
        "not enough arrows",
    ),
]

submit_cases = run_cases + [
    (Wizard("Hermoine", 45, 25), Archer("Achilles", 60, 1), ["cast"], [45, 35]),
    (
        Wizard("Dumbledore", 100, 150),
        Archer("Hercules", 120, 4),
        ["shoot"],
        [90, 120],
    ),
    (
        Wizard("Snape", 80, 24),
        Archer("Theseus", 70, 3),
        ["cast"],
        [None, None],
        "not enough mana",
    ),
    (
        Wizard("Luna", 65, 49),
        Archer("Paris", 85, 2),
        ["cast", "shoot", "shoot", "cast"],
        [None, None],
        "not enough mana",
    ),
    (
        Wizard("Neville", 55, 45),
        Archer("Hector", 75, 3),
        ["shoot", "cast"],
        [45, 50],
    ),
]


def test(wizard, archer, actions, expected_result, expected_err=None):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * Wizard: {wizard.get_name()}, HP: {wizard.get_health()}")
    print(f" * Archer: {archer.get_name()}, HP: {archer.get_health()}")
    print(f"Actions: {actions}")

    try:
        for action in actions:
            if action == "cast":
                print(f"{wizard.get_name()} casts a spell at {archer.get_name()}")
                wizard.cast(archer)
            elif action == "shoot":
                print(f"{archer.get_name()} shoots an arrow at {wizard.get_name()}")
                archer.shoot(wizard)

        if expected_err:
            print(f"Expected Exception: {expected_err}")
            print("Actual: no exception raised")
            print("Fail")
            return False

        wizard_hp = wizard.get_health()
        archer_hp = archer.get_health()
        print(
            f"Expected: {wizard.get_name()} HP: {expected_result[0]}, {archer.get_name()} HP: {expected_result[1]}"
        )
        print(
            f"Actual: {wizard.get_name()} HP: {wizard_hp}, {archer.get_name()} HP: {archer_hp}"
        )

        if wizard_hp == expected_result[0] and archer_hp == expected_result[1]:
            print("Pass")
            return True
        else:
            print("Fail")
            return False

    except Exception as e:
        print(f"Expected Exception: {expected_err}")
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
