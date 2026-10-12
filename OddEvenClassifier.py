odd_numbers = []
even_numbers = []
exit_loop = False


def design():
    print("=" * 30)

def input_numbers(odd_number, even_number):
        number = (input("Enter a Number: "))
        if number == "done":
            return True
        try:
            number = int(number)
            if number % 2 == 0:
                even_number.append(number)
            else:
                odd_number.append(number)
        except ValueError:
            print("Invalid Input!")

while True:
    exit_loop = input_numbers(odd_numbers, even_numbers,)

    if exit_loop:
        break

design()
print("      NUMBER CLASSIFIER      ")
design()
print(f"Even Numbers ({len(even_numbers)}) : {even_numbers}")
print(f"Odd Numbers  ({len(odd_numbers)}) : {odd_numbers}")
