
new_entries = []

def load_diary_history():
    try:
        with open("diary.txt", "r") as file:
            content = file.read()
            print("--- Past Entries ---")
            print(content)
            print("-" * 20)
    except FileNotFoundError:
        print("No past entries found. Starting a fresh diary!")

def save_new_entries(text):
    with open("diary.txt", "a") as file:
        for sentence in text:
            file.write(sentence + "\n")

load_diary_history()

while True:
    line = input("Write a line for your diary (or type 'save' to quit) : ")
    if line =="save":
        save_new_entries(new_entries)
        break
    else:
        new_entries.append(line)

