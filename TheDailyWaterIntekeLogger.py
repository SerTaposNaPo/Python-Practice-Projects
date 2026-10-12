from datetime import date



def load_water_log():
    water_data_log = {}
    try:
        with open("water_log.txt", "r") as file:
            for content in file:
                clean_line = content.strip()
                parts = clean_line.split(":")
                water_data_log[parts[0]] = int(parts[1])
                print(content)

    except FileNotFoundError:
        print("No past entries found. Starting a fresh data!")

    return water_data_log

def save_water_log(data):
    with open("water_log.txt", "w") as file:
        for date, water in data.items():
            file.write(f"{date}:{water}\n")

water_data = load_water_log()
while True:
    water = input("How many mL did you drink? : ")
    today = str(date.today())
    if water == "save":
        save_water_log(water_data)
        break

    if today in water_data:
        water_data[today] += int(water)
    else:
        water_data[today] = int(water)



