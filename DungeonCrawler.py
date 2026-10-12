import os
import random

board = [
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", "."],
]

player_x = random.randint(0, 6)
player_y = random.randint(0, 6)
trap_x = random.randint(0, 6)
trap_y = random.randint(0, 6)
monster_x = random.randint(0, 6)
monster_y = random.randint(0, 6)
exit_x = random.randint(0, 6)
exit_y = random.randint(0, 6)


entity_state = {
    "Player": {"X": player_x, "Y": player_y, "HP": 100},
    "Trap": {"X": trap_x, "Y": trap_y},
    "Monster": {"X": monster_x, "Y": monster_y},
    "Exit": {"X": exit_x, "Y": exit_y}
}


def game_loop():

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        for r, row in enumerate(board):
            for c, column in enumerate(row):
                if r == entity_state["Player"]["Y"] and c == entity_state["Player"]["X"]:
                    print("P  ", end="")
                elif r == entity_state["Trap"]["Y"] and c == entity_state["Trap"]["X"]:
                    print("T  ", end="")
                elif r == entity_state["Monster"]["Y"] and c == entity_state["Monster"]["X"]:
                    print("M  ", end="")
                elif r == entity_state["Exit"]["Y"] and c == entity_state["Exit"]["X"]:
                    print("E  ", end="")
                else:
                    print(".  ", end="")
            print()
        print(F"HP: {entity_state["Player"]["HP"]}")
        move = input("Move (W/A/S/D): ").lower()
        if move == "w":
            if entity_state["Player"]["Y"] == 0:
                entity_state["Player"]["Y"] = entity_state["Player"]["Y"]
            else:
                entity_state["Player"]["Y"] -= 1
        elif move == "s":
            if entity_state["Player"]["Y"] == 6:
                entity_state["Player"]["Y"] = entity_state["Player"]["Y"]
            else:
                entity_state["Player"]["Y"] += 1
        elif move == "a":
            if entity_state["Player"]["X"] == 0:
                entity_state["Player"]["X"] = entity_state["Player"]["X"]
            else:
                entity_state["Player"]["X"] -= 1
        elif move == "d":
            if entity_state["Player"]["X"] == 6:
                entity_state["Player"]["X"] = entity_state["Player"]["X"]
            else:
                entity_state["Player"]["X"] += 1
        chance = random.randint(1, 10)
        if chance <= 7:
            if entity_state["Player"]["X"] > entity_state["Monster"]["X"]:
                entity_state["Monster"]["X"] += 1
            elif entity_state["Player"]["X"] < entity_state["Monster"]["X"]:
                entity_state["Monster"]["X"] -= 1
            elif entity_state["Player"]["Y"] > entity_state["Monster"]["Y"]:
                entity_state["Monster"]["Y"] += 1
            elif entity_state["Player"]["Y"] < entity_state["Monster"]["Y"]:
                entity_state["Monster"]["Y"] -= 1
        else:
            if entity_state["Player"]["X"] > entity_state["Monster"]["X"]:
                entity_state["Monster"]["X"] += 1
            if entity_state["Player"]["X"] < entity_state["Monster"]["X"]:
                entity_state["Monster"]["X"] -= 1
            if entity_state["Player"]["Y"] > entity_state["Monster"]["Y"]:
                entity_state["Monster"]["Y"] += 1
            if entity_state["Player"]["Y"] < entity_state["Monster"]["Y"]:
                entity_state["Monster"]["Y"] -= 1

        if entity_state["Player"]["X"] == entity_state["Trap"]["X"]:
            if entity_state["Player"]["Y"] == entity_state["Trap"]["Y"]:
                entity_state["Player"]["HP"] -= 20
                print("You stepped on a trap!")
        if entity_state["Player"]["X"] == entity_state["Monster"]["X"]:
            if entity_state["Player"]["Y"] == entity_state["Monster"]["Y"]:
                print("You got eaten!")
                print("Game Over")
                input("Press Any key to continue...")
                break
        if entity_state["Player"]["HP"] == 0:
            print("You died!")
            print("Game Over")
            input("Press Any key to continue...")
            break
        if entity_state["Player"]["X"] == entity_state["Exit"]["X"]:
            if entity_state["Player"]["Y"] == entity_state["Exit"]["Y"]:
                print("You Escaped! You Win!")
                break



game_loop()