# The main storage
bag = ["Sword", "Potion", "Shield", "Bow"]

# Main interface
def interface():
    while True: # Loop
        try:
            print("##--Inventory--##")
            print("1. View Inventory")
            print("2. Add Item")
            print("3. Remove Item")
            print("4. Exit")
            choice = int(input("Input: "))  # Request the user to input there choice
            if 1 <= choice <= 4:
                if choice == 1:
                    inventory(bag)
                    break
                elif choice == 2:
                    Additem(bag)
                    break
                elif choice == 3:
                    Remitem(bag)
                    break
                elif choice == 4:
                    print("Goodbye")
                    break
        except ValueError:
            print("Invalid choice, please try again.")

# Inventory interface
def inventory (olbag,):# olbag is just a place holder
    for item in olbag:
        print(item)
    while True:
        print("Back to Main Menu?")
        print("1. Yes")
        print("2. NO")
        choice = int(input(": "))
        if choice == 1:
            interface()
        elif choice == 2:
            print("Thank You")
            break

# Add item
def Additem (bag):
    Item = input("Add New Item: ")
    bag.append(Item)
    interface()


# Remove item
def Remitem (bag):
    for item in bag:
        print(item)
    item = input("Remove Item: ")
    bag.remove(item)
    interface()

interface()