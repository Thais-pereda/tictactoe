"""A class to control the game commands"""

import pyinputplus as pyip


class Game:

    def __init__(self):
        print("Welcome to tic-tac-toe.")
        self.free_cells = ["top-left", "top-middle", "top-right", "middle-left", "center", "middle-right", "bottom-left", "bottom-middle", "bottom-right"]
        self.turn = 1
        self.top = ['', '', '']
        self.middle = ['', '', '']
        self.bottom = ['', '', '']

    def start_game(self, playerone, playertwo):
        self.first_move(playerone, playertwo)
        while not self.game_over():
            if self.turn == 1:
                print(f"{playerone} turn.")
                position = self.player_move()
                self.update_board("X", position)
                self.free_cells.remove(position)
                self.print_board()
                self.turn = 2
                self.start_game(playerone, playertwo)
            elif self.turn == 2:
                print(f"{playertwo} turn.")
                position = self.player_move()
                self.update_board("O", position)
                self.free_cells.remove(position)
                self.print_board()
                self.turn = 1
                self.start_game(playerone, playertwo)
        if self.turn == 2:
            return f"{playerone} wins"
        elif self.turn == 1:
            return f"{playertwo} wins"

    def first_move(self, playerone, playertwo):
        if self.turn == 1:
            print(f"{playerone} turn.")
            position = self.player_move()
            self.update_board("X", position)
            self.free_cells.remove(position)
            self.print_board()
            self.turn = 2
        elif self.turn == 2:
            print(f"{playertwo} turn.")
            position, free_cells = self.player_move()
            self.update_board("O", position)
            self.free_cells = free_cells
            self.print_board()
            self.turn = 1

    def player_move(self):
        print("Choose a cell to place your marker: ", *self.free_cells, sep=" | ")
        next_turn = False
        while not next_turn:
            position: str = input()
            if position.lower() not in self.free_cells:
                print("Invalid command. Try again.")
                continue
            else:
                next_turn = True
        return position


    def update_board(self, marker, position):
        if position == "top-left":
            self.top[0] = marker
        elif position == "top-middle":
            self.top[1] = marker
        elif position == "top-right":
            self.top[2] = marker
        elif position == "middle-left":
            self.middle[0] = marker
        elif position == "center":
            self.middle[1] = marker
        elif position == "middle-right":
            self.middle[2] = marker
        elif position == "bottom-left":
            self.bottom[0] = marker
        elif position == "bottom-middle":
            self.bottom[1] = marker
        elif position == "bottom-right":
            self.bottom[2] = marker


    def print_board(self):
        print(*self.top, sep=" | ")
        print("-------")
        print(*self.middle, sep=" | ")
        print("-------")
        print(*self.bottom, sep=" | ")

    def game_over(self):
        if self.top[0] == self.top[1] and self.top[1] == self.top[2]:
            if self.top[0] != "":
                return True
        elif self.middle[0] == self.middle[1] and self.middle[1] == self.middle[2]:
            if self.middle[0] != "":
                return True
        elif self.bottom[0] == self.bottom[1] and self.bottom[1] == self.bottom[2]:
            if self.bottom[0] != "":
                return True
        elif self.top[0] == self.middle[0] and self.middle[0] == self.bottom[0]:
            if self.top[0] != "":
                return True
        elif self.top[1] == self.middle[1] and self.middle[1] == self.bottom[1]:
            if self.top[1] != "":
                return True
        elif self.top[2] == self.middle[2] and self.middle[2] == self.bottom[2]:
            if self.top[2] != "":
                return True
        elif self.top[0] == self.middle[1] and self.middle[1] == self.bottom[2]:
            if self.top[0] != "":
                return True
        elif self.top[2] == self.middle[1] and self.middle[1] == self.bottom[0]:
            if self.top[2] != "":
                return True
        else:
            return False

    def new_game(self):
        new_game = pyip.inputYesNo("Play again? Yes or No: ")
        if new_game == 'yes':
            return True
        elif new_game == 'no':
            return False




