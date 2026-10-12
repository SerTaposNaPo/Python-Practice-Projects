# Current ingredients left in the kitchen
cafe_stock = {
    "Espresso Shots": 10,
    "Milk (oz)": 32,
    "Croissants": 3,
    "Avocado": 0
}

# What each menu combo requires
menu_combos = {
    "Iced Latte": {"Espresso Shots": 2, "Milk (oz)": 8},
    "Breakfast Deal": {"Espresso Shots": 1, "Croissants": 1},
    "Avocado Toast Box": {"Avocado": 1, "Croissants": 1}
}


def complete_order(combo_name):
    # 1. Check if the combo exists in the menu_combos dictionary
    if combo_name not in menu_combos:
        print(f"Error! {combo_name} is not on the menu.")
        return

    # 2. Get the specific ingredients dictionary for this combo
    order_requirements = menu_combos[combo_name]

    # --- YOUR CODE GOES HERE ---
    # Step A: Loop through order_requirements to check if cafe_stock has enough.
    for ingredient, stock in order_requirements.items():
        order = cafe_stock.get(ingredient, 0)
        if order < stock:
            print(f"Error! We only has {order} {ingredient} left")
            return

    #         If not enough, print the error and return early.

    # Step B: If ALL ingredients are available, loop again to subtract them
    #         from cafe_stock and print a success message.
    for ingredient, stock in order_requirements.items():
        cafe_stock[ingredient] -= stock

    print(f"You successfully order {combo_name}")

# --- Test Cases to run your code ---
print("Initial Stock:", cafe_stock)
print("-" * 40)

# Test 1: Should succeed!
complete_order("Breakfast Deal")
print("Stock after Test 1:", cafe_stock)
print("-" * 40)

# Test 2: Should fail (Not enough avocado!)
complete_order("Avocado Toast Box")

# Test 3: Should fail (Menu item doesn't exist)
complete_order("Pizza Combo")