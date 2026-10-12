grades = []

def total_average(list_of_scores):
    total_grades = 0
    for grade in list_of_scores:
        total_grades += grade
    return total_grades / len(list_of_scores)

def evalution(average):
    if average >= 90:
        return "You got an A"
    elif average >= 80:
        return "You got an B"
    elif average >= 70:
        return "You got an C"
    elif average >= 60:
        return "You got an D"
    elif average >= 50:
        return "You got an E"
    else:
        return "You got an F"

name = input("Student Name: ")
print("Type -1 if done")
while True:
    try:
        score = int(input("Input the score : "))
        if score == -1:
            break
        grades.append(score)
    except ValueError:
        print("Please Enter Numbers!")

final_score = total_average(grades)

print("="*30)
print(f"STUDENT REPORT CARD: {name}")
print("="*30)
print(f"Average Score: {final_score:.2f}")
print(f"Final Grade: {evalution(final_score)}")
print(f"Highest Test: {max(grades)}")
print(f"Lowest Test: {min(grades)}")
print("="*30)