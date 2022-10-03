#Hannah Millward
#August 2022
#Calculate charge based on distance travelled

import math

cost = 10
cost = int(cost)

def round_decimals_up(distance):
    """
    Returns a value rounded up to a specific number of decimal places.
    """
    factor = 10 ** 0
    rounded_distance = math.ceil(distance * factor) / factor
    return rounded_distance

distance = float(input("Distance Travelled: "))

if distance < 0 or distance > 100:
    print("Please enter a number betwen 0 and 100")
else:
    if (distance % 1) < .5:
        rounded_distance = round(distance)
    else:
        rounded_distance = round_decimals_up(distance)
    print(rounded_distance)

    if rounded_distance <= 5:
        print(cost)
    else:
        distance_to_pay = rounded_distance - 5
        cost += distance_to_pay * .5
        print(cost)
