from main import *

run_cases = [
    ("Faramir", "Human", None),
    ("Bard", "Archer", 1),
]

submit_cases = run_cases + [
    ("Legolas", "Archer", 5),
    ("Boromir", "Human", None),
    ("Aragorn", "Human", None),
    ("Gimli", "Human", None),
    ("Frodo", "Human", None),
    ("Robin", "Archer", 10),
]


def test(name, type, num_arrows):
    print("---------------------------------")
    print(f"Name: {name} | type: {type} | num_arrows: {num_arrows}")
    try:
        if type == "Human":
            human = Human(name)
            print(f"Expecting Human: {name}")
            print(f"Actual: {human.get_name()}")
            if human.get_name() == name:
                print("Pass")
                return True
            else:
                print("Fail")
                return False
        else:
            archer = Archer(name, num_arrows)
            print(f"Expecting Archer: {name} with {num_arrows} arrows")
            print(f"Actual: {archer.get_name()} with {archer.get_num_arrows()} arrows")
            if archer.get_name() == name and archer.get_num_arrows() == num_arrows:
                print("Pass")
                return True
            else:
                print("Fail")
                return False
    except Exception as e:
        print(f"Error: {e}")
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
