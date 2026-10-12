# The items currently in the player's backpack
player_inventory = {
    "Wood": 5,
    "Stone": 3,
    "Iron Ore": 1,
    "String": 0
}

# What is required to make advanced items
crafting_recipes = {
    "Wooden Sword": {"Wood": 3},
    "Pickaxe": {"Wood": 2, "Stone": 3},
    "Lantern": {"Iron Ore": 2, "Wood": 1}
}

# Function that check what you want to craft
def craft_item(item_name):
    if item_name not in crafting_recipes: # If the item you put is not in the crafting recipe
        print(f"Error! the {item_name} is not in the recipies") # it will print this
        return # Return the values it gets

    recipe = crafting_recipes[item_name] # Will make a new variable name recipe that find the item_name inside crafting_recipes

    for item, amount_needed in recipe.items(): # The .items() say that it will look inside the another dictionary inside crafting_recipes and put the item and amount as its placeholder name
        player_has = player_inventory.get(item, 0) # Use to get the value of item needed in the crafting_recipes

        if player_has < amount_needed: # If the Value of the crafting_recipes is less than the amount needed to craft
            left_over = amount_needed - player_has # It subtracts the amount_needed to amount that the crafting_recipes has
            print(f"Failed! You need {left_over} more {item} to make a {item_name}.") # It prints the message that it failed crafting and display the amount of item needed
            return # Return the values it gets

    for item, amount_needed in recipe.items(): # The .items() say that it will look inside the another dictionary inside crafting_recipes and put the item and amount as its placeholder name
        player_inventory[item] -= amount_needed # It goes to the player_inventory and search for item, then subtract the amount_needed or the amount that is previously used in crafting the item

    player_inventory[item_name] = player_inventory.get(item_name, 0) + 1  # It goes to the player_inventory and search for item_name then add it or its value if it's already there

    print(f"The {item_name} is added to your inventory")



# --- Test Cases to run your code ---
print("Initial Inventory:", player_inventory)
print("-" * 30)

# Test 1: This should succeed!
craft_item("Pickaxe")
print("Inventory after Pickaxe:", player_inventory)
print("-" * 30)

# Test 2: This should fail because they don't have enough Iron Ore!
craft_item("Lantern")

# Test 3: This should fail because the recipe doesn't exist!
craft_item("Spaceship")

