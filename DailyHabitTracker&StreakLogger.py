
def load_habits():
    habits_dict = {}
    try:
        print(" --- HOBBIES --- ")
        with open("habit.txt", "r") as file:
            for line in file:
                clean_line = line.rstrip()
                if clean_line == "":
                    continue
                parts = clean_line.split(":")
                habits_dict[parts[0]] = int(parts[1])
                print(f"{parts[0]}  :  {parts[1]}")

    except FileNotFoundError:
        print("Starting a fresh tracker")

    return habits_dict

def save_habits(habits_dict):
    with open("habit.txt", "w") as file:
        for habit, streak in habits_dict.items():
            file.write(f"{habit}:{streak}\n")


my_habits = load_habits()
while True:
    habit_input = input("Enter a habit you finished today (or type 'save' to quit) : ")
    if habit_input ==  "save":
        save_habits(my_habits)
        break
    if habit_input in my_habits:
        my_habits[habit_input] += 1
    else:
        my_habits[habit_input] = 1





