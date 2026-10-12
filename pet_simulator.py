

def main():
    print("=== Pet Simulator ===")
    name = input("Input the pets name : ")
    age = input("Input the age : ")
    my_pet = Pet(name, age)
    my_pet.check_status()
    run_game(my_pet)



class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hunger_level = 50
        self.energy_level = 50
        self.happiness_level = 50


    def feed(self):
        self.hunger_level -= 10
        self.happiness_level += 10
        if self.hunger_level < 0:
            self.hunger_level = 0
        if self.hunger_level > 100:
            self.hunger_level = 100
        if self.happiness_level < 0:
            self.happiness_level = 0
        if self.happiness_level > 100:
            self.happiness_level = 100

    def play(self):
        self.happiness_level += 20
        self.hunger_level += 10
        self.energy_level -= 20
        if self.hunger_level < 0:
            self.hunger_level = 0
        if self.hunger_level > 100:
            self.hunger_level = 100
        if self.happiness_level < 0:
            self.happiness_level = 0
        if self.happiness_level > 100:
            self.happiness_level = 100
        if self.energy_level < 0:
            self.energy_level = 0
        
    def sleep(self):
        self.energy_level = 100
        if self.energy_level < 0:
            self.energy_level = 0


    def check_status(self):
        print()
        print(f"{self.name} Attributes")
        print(f"Age : {self.age}")
        print(f"Hunger Level : {self.hunger_level}")
        print(f"Energy Level : {self.energy_level}")
        print(f"Happiness Level : {self.happiness_level} ")
        print()


def run_game(pet):
    while True:
        activity = input("What do you want to do : ")
        if activity == "feed":
            pet.feed()
            pet.check_status()
        elif activity == "play":
            pet.play()
            pet.check_status()
        elif activity == "sleep":
            pet.sleep()
            pet.check_status()
        elif activity == "exit":
            break
        else:
            print("Invalid Input")



if __name__ == "__main__":
    main()