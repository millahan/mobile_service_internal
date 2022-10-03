#Hannah Millward
#August 2022
#Calculate charge based on minutes travlled

cost = 0

wof = input("Was WOF required? (y or n): ")
if wof == 'y':
    cost += 100
    print(f"Wof cost: {cost}")
else:
    print(f"Wof cost: {cost}")
    

virus = input("Was Virus Protection required? (y or n): ")
if virus == 'y':
    minutes = int(input("Minutes: "))
    if minutes <= 0 or minutes > 480:
        print("Please enter a number betwen 0 and 100")
    else:
        minutes_fee = minutes * .8
        cost += minutes_fee
        print(f"Wof and virus cost: {cost:.2f}")
else:
    print(f"Wof and virus cost: {cost:.2f}")

print(f"Total: {cost}")

