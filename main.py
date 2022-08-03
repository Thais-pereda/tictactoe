"""tictactoe - a text-based version of the Tic Tac Toe game. """

from game import Game

new_game = True


while new_game:
    game = Game()
    playerone = input("Player one: ")
    playertwo = input("Player two: ")
    winner = game.start_game(playerone, playertwo)
    print(winner)
    new_game = game.new_game()

print("Thank you for playing!")




