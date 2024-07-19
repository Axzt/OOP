from main import *

run_cases = [
    ("Merlin", 10, 10, 1000, 100),
    ("Morgana", 20, 5, 2000, 50),
]

submit_cases = run_cases + [
    ("Arthur", 3, 3, 300, 30),
]


def test(
    wizard_name,
    wizard_stamina,
    wizard_intelligence,
    expected_health,
    expected_mana,
):
    print("---------------------------------")
    print(f"Wizard({wizard_name}, {wizard_stamina}, {wizard_intelligence})")
    wizard = Wizard(wizard_name, wizard_stamina, wizard_intelligence)
    print(f"Expected mana: {expected_mana}")
    print(f"Actual mana: {wizard.mana}")
    print(f"Expected health: {expected_health}")
    print(f"Actual health: {wizard.health}")
    if wizard.mana != expected_mana:
        return False
    if wizard.health != expected_health:
        return False
    return True


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
