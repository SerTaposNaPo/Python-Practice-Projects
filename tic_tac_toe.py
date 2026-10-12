def main():
    board = Board()
    current_player = "X"
    while True:
        board.display()
        row = int(input("Row : "))
        col = int(input("Column : "))
        move = board.place_mark(row, col, current_player)
        if not move:
            print("Invalid Move, Try Again")
        else:
            winner = board.check_winner()
            if winner  is not None:
                print(f"{winner} Wins")
                break
            elif board.is_full():
                print("It's a draw!")
                break
            else:
                if current_player == "X":
                    current_player = "O"
                else:
                    current_player = "X"


class Board:
    def __init__(self):
        self.grid = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    def display(self):
        for row in self.grid:
            print(row)

    def place_mark(self, row, col, mark):
        if row > 2 or col > 2:
            return False
        elif row < 0 or col < 0:
            return False
        else:
            self.grid[row][col] = mark
            return True

    def check_winner(self):
        for row in self.grid:
            if row[0] == row[1] == row[2] != " ":
                return row[0]
        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] != " ":
                return self.grid[0][col]
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != " ":
            return self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != " ":
            return self.grid[0][2]
        return None

    def is_full(self):
        for row in self.grid:
            for cell in row:
                if cell == " ":
                    return False
        return True

if __name__ == "__main__":
    main()