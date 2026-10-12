# How many copies are currently left on the shelf
library_inventory = {
    "Introduction to Python": 2,
    "Data Structures 101": 1,
    "AI Foundations": 0,
    "Clean Code Manual": 5
}

# The books needed for specific research topics
project_bundles = {
    "Data Science Basics": {"Introduction to Python": 1, "Data Structures 101": 1},
    "Machine Learning Track": {"Introduction to Python": 1, "AI Foundations": 1},
    "Software Engineering Pro": {"Clean Code Manual": 1, "Data Structures 101": 2}
}

def checkout_bundle(project):
    if project not in project_bundles:
        print(f"The {project} is not in the Library")
        return

    bundle = project_bundles[project]

    for book, amount_needed in bundle.items():
        book_stock = library_inventory.get(book, 0)

        if book_stock < amount_needed:
            print(f"Sorry but we dont have enough {project} bundle")
            return

    for book, amount_needed in bundle.items():
        library_inventory[book] -= amount_needed

    print(f"You successfully borrow the {project} bundle")

# --- Test Cases to run your code ---
print("Initial Library Inventory:", library_inventory)
print("-" * 50)

# Test 1: Should succeed! (Python and Data Structures both drop by 1)
print("Testing: Data Science Basics")
checkout_bundle("Data Science Basics")
print("Inventory after Test 1:", library_inventory)
print("-" * 50)

# Test 2: Should fail! (AI Foundations has 0 copies available)
print("Testing: Machine Learning Track")
checkout_bundle("Machine Learning Track")
print("-" * 50)

# Test 3: Should fail! (Needs 2 copies of Data Structures, but only 0 left after Test 1)
print("Testing: Software Engineering Pro")
checkout_bundle("Software Engineering Pro")
print("-" * 50)

# Test 4: Should fail! (Bundle doesn't exist)
print("Testing: Game Dev Kit")
checkout_bundle("Game Dev Kit")