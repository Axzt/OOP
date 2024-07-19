from main import *

run_cases = [
    (Wall(2, 3, 4), 24),
    (Wall(3, 4, 5), 60),
    (Wall(4, 5, 6), 120),
    (Wall(1, 2, 3), 6),
]

submit_cases = run_cases + [
    (Wall(7, 8, 9), 504),
    (Wall(10, 11, 12), 1320),
    (Wall(13, 14, 15), 2730),
    (Wall(16, 17, 18), 4896),
    (Wall(19, 20, 21), 7980),
    (Wall(22, 23, 24), 12144),
]


def test(wall, expected_output):
    print("---------------------------------")
    try:
        volume = wall.volume
        print(
            f"A wall with {wall.depth} depth, {wall.height} height, {wall.width} width"
        )
        print(f"Expected volume: {expected_output}")
        print(f"Actual volume: {volume}")
        if expected_output == volume:
            print("Pass")
            return True
    except Exception as e:
        print(f"Error: {e}")
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
