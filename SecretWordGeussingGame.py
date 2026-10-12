secret_word = ["p","y","t","h","o","n"]

guess_word = []

live = 0

print("---Guess The Word---")


while True:

    has_won = True

    for word in secret_word:
        if word in guess_word:
            print(f" {word.upper()} ", end="")
        else:
            print(" _ ", end="")
            has_won = False
    print()

    if has_won:
        print()
        print("You Win!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guess_word:
        print(f"You already guess {guess}")
    elif not guess.isalpha():
        print("That is not a valid letter! Please type a-z only")
    elif len(guess) > 1:
        print("Please type only ONE letter at a time")
    elif guess in secret_word:
        print("Correct!")
        guess_word.append(guess)
    elif guess not in secret_word:
        print(f"{guess} is not in the word")
        live += 1

    if live == 5:
        print()
        print("The word is ", end="")
        for letter in secret_word:
            print(letter, end="")
        print()
        print("You lose :(")
        break
