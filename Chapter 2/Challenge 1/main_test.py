from main import *

run_cases = [
    ("1234567890", 100.0, 50.0, 75.0, 75.0),
    ("0987654321", 500.0, 100.0, 200.0, 400.0),
]

submit_cases = run_cases + [
    ("1234567890", 100.0, 50.0, 200.0, 150.0, None, "Insufficient funds"),
    ("0987654321", 500.0, 500.0, 500.0, 500.0),
    ("1234567890", 300.0, -10.0, 20.0, 280.0, "Cannot deposit zero or negative funds"),
    ("0987654321", 200.0, 0.0, 10.0, 190.0, "Cannot deposit zero or negative funds"),
    ("1234567890", -20.0, 10.0, 10.0, -10.0, None, "Insufficient funds"),
    (
        "0987654321",
        100.0,
        10.0,
        -10.0,
        110.0,
        None,
        "Cannot withdraw zero or negative funds",
    ),
    (
        "1234567890",
        900.0,
        100.0,
        0.0,
        1000.0,
        None,
        "Cannot withdraw zero or negative funds",
    ),
]


def test(
    account_number,
    initial_balance,
    deposit_amount,
    withdraw_amount,
    expected_balance,
    deposit_err=None,
    withdraw_err=None,
):
    print("---------------------------------")
    try:
        print(
            f"Inputs: account_number: {account_number}, initial_balance: {initial_balance:.2f}, deposit_amount: {deposit_amount:.2f}, withdraw_amount: {withdraw_amount:.2f}"
        )
        account = BankAccount(account_number, initial_balance)
        try:
            account.deposit(deposit_amount)
            if deposit_err:
                print(f'Expected error "{deposit_err}"')
                print(f"Actual output: No error was raised")
                print("Fail")
                return False
        except ValueError as e:
            print(f'Expected error "{deposit_err}"')
            print(f'Actual error "{e}"')
            if str(e) != deposit_err:
                print("Fail")
                return False
        try:
            account.withdraw(withdraw_amount)
            if withdraw_err:
                print(f'Expected error "{withdraw_err}"')
                print(f"Actual output: No error was raised")
                print("Fail")
                return False
        except ValueError as e:
            print(f'Expected error "{withdraw_err}"')
            print(f'Actual error "{e}"')
            if str(e) != withdraw_err:
                print("Fail")
                return False
        print(f"Expected balance ${expected_balance:.2f}")
        print(f"Actual balance ${account.get_balance():.2f}")
        if account.get_balance() != expected_balance:
            print("Fail")
            return False
        print("Pass")
        return True
    except Exception as e:
        print(f"Fail: {e}")
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
