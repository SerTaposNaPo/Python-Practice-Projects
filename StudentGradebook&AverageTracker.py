

def load_grades():
    gradebook = {}
    try:
        with open("grades.txt", "r") as file:
            for grades in file:
                clean_line = grades.strip()
                parts = clean_line.split(":")

                name = parts[0]
                grades_string = parts[1]

                grades_list = grades_string.split(",")
    except FileNotFoundError:
        print("No past entries found. Starting a fresh data!")

    return gradebook

def gradebook_dict():
    with open("grades.txt", "w") as file:
        pass

my_gradebook = load_grades()
while True:
    name = input("Name : ")
    if name == "save":
        break
    grade = int(input("Grade : "))
    if name in my_gradebook:
        my_gradebook[name].append(grade)
    else:
        my_gradebook[name] = [grade]



