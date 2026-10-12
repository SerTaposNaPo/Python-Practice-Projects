distance = []
delStop = 0
print("=== Shift Expense Tracker Started ===")

while True:
    try:
        stop = float(input(f"Enter distance for Stop {delStop + 1} (or 0 to finish shift): "))
        distance.append(stop)
        if stop >= 1:
            delStop += 1
            print(f"Stop added! Current stops logged: {delStop}")
        print()
        if stop == 0:
            total = sum(distance)
            fuelConsump = total / 12
            gasCost = fuelConsump * 60
            print("=== EOD ROUTE SUMMARY REPORT ===")
            print(f"Total Deliveries Made  : {delStop}")
            print(f"Total Distance Covered : {total:.2f} km" )
            print(f"Total Fuel Consumed    : {fuelConsump:.2f} liters")
            print(f"Total Route Gas Cost   : {gasCost:.2f} PHP")
            print("================================")
            break
    except ValueError:
        print("[Error] Please enter a valid number for distance.")
        print()

