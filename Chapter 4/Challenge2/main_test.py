from main import *

run_cases = [
    (Siege(100, 10), 100, 4, 40, None),
    (BatteringRam(100, 10, 2000, 5), 100, 5, 70, 10),
    (Catapult(100, 10, 2), 100, 6, 60, 2),
]

submit_cases = run_cases + [
    (Siege(60, 5), 100, 2, 40, None),
    (BatteringRam(80, 5, 2000, 4), 100, 4, 100, 8),
    (Catapult(90, 4, 3), 100, 10, 250, 3),
]


def test(vehicle, distance, fuel_price, expected_cost, expected_cargo_volume):
    try:
        vehicle_type = vehicle.__class__.__name__
        print("---------------------------------")
        print(
            f"Testing {vehicle_type}: Max Speed {vehicle.max_speed} kph, Efficiency {vehicle.efficiency} km/food"
        )
        print(f"Distance: {distance} km, Price: {fuel_price} per food")
        print(
            f"Expected: Trip Cost: {expected_cost}, Cargo Volume: {expected_cargo_volume}"
        )
        actual_cost = int(vehicle.get_trip_cost(distance, fuel_price))
        actual_cargo_volume = vehicle.get_cargo_volume()
        if actual_cargo_volume is not None:
            actual_cargo_volume = int(actual_cargo_volume)
        print(
            f"  Actual: Trip Cost: {actual_cost}, Cargo Volume: {actual_cargo_volume}"
        )
        if (
            actual_cost == expected_cost
            and expected_cargo_volume == actual_cargo_volume
        ):
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
