from main import *

run_cases = [
    (10, [("add", 5), ("subtract", 3)], 12),
    (5, [("multiply", 2), ("divide", 2)], 5),
]

submit_cases = run_cases + [
    (10, [("divide", 0)], None, "Cannot divide by zero"),
    (7, [("modulo", 4)], 3),
    (10, [("power", 3)], 1000),
    (99, [("clear", None), ("power", 2)], 0),
    (9, [("square_root", None), ("add", 5)], 8),
]

actions = {
    "add": Calculator.add,
    "subtract": Calculator.subtract,
    "multiply": Calculator.multiply,
    "divide": Calculator.divide,
    "modulo": Calculator.modulo,
    "power": Calculator.power,
    "square_root": Calculator.square_root,
    "clear": Calculator.clear,
}


def test(starting_num, actions_list, expected_output, expected_err=None):
    print("---------------------------------")
    print(f"Starting Number: {starting_num}, Actions: {actions_list}")
    calculator = Calculator()
    calculator.add(starting_num)
    try:
        result = calculator.result
        print("'result' attribute is not private")
        print("Fail 3")
        return False
    except Exception as e:
        if str(e) != "'Calculator' object has no attribute 'result'":
            print("Exception: " + str(e))
            print("Fail 4")
            return False
    try:
        for action, number in actions_list:
            if number is None:
                actions[action](calculator)
            else:
                actions[action](calculator, number)
        result = calculator.get_result()
        print(f"Expected Output: {expected_output}")
        print(f"Actual Output: {result}")
        if float(result) == float(expected_output):
            print("Pass 1")
            return True
        else:
            print("Fail 1")
            return False
    except Exception as e:
        actual_err = str(e)
        print(f"Expected Error: {expected_err}")
        print(f"Actual Error: {actual_err}")
    if actual_err == expected_err:
        print("Pass 2")
        return True
    else:
        print("Fail 2")
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
