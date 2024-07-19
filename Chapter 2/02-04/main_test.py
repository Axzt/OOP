from main import *

run_cases = [
    ("Merlin", 10, 10, 500, 200),
    ("Morgana", 20, 5, 1500, 150),
]

submit_cases = run_cases + [
    ("Arthur", 3, 3, -200, 130),
]


def test(
    wizard_name,
    wizard_stamina,
    wizard_intelligence,
    expected_health_after,
    expected_mana_after,
):
    print("---------------------------------")
    print(f"Wizard({wizard_name}, {wizard_stamina}, {wizard_intelligence})")
    wizard = Wizard(wizard_name, wizard_stamina, wizard_intelligence)
    wizard.get_fireballed()
    wizard.drink_mana_potion()
    print(f"Expected health after: {expected_health_after}")
    print(f"Actual health after: {wizard.health}")
    print(f"Expected mana after: {expected_mana_after}")
    print(f"Actual mana after: {wizard.mana}")
    if wizard.health != expected_health_after:
        return False
    if wizard.mana != expected_mana_after:
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
