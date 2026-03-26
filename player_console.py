import sys
from output_console import *
from input_console import InputConsole
from game_state import GameState
from player_base import PlayerBase
from input_base import Keys
from util import Util

if Util.isRaspberry():
    from input_sensehat import InputSenseHat
    from output_sensehat import OutputSenseHat


class PlayerConsole(PlayerBase):
    def __init__(self, player: GameToken):  # Red or Yellow player
        super().__init__(player)
        
        self._output = OutputConsole() # use this class for console output
        self._input = InputConsole() # use this class for console input
        self._current_col = 3  # Start in the middle column for the 'ghost' token   

    def play_turn(self) -> int:
        # YOUR CODE HERE
        # TODO: return desired column from user input (0..6) using
        # use self._input to read keys, use self._output to draw current token position
        while True:
            self._output.draw_token(self._current_col, -1, self._player)
            key = self._input.read_key()

            if key == Keys.LEFT and self._current_col > 0:
                self._output.draw_token(self._current_col, -1, GameToken.EMPTY)
                self._current_col -= 1
            elif key == Keys.RIGHT and self._current_col < 6:
                self._output.draw_token(self._current_col, -1, GameToken.EMPTY)
                self._current_col += 1
            elif key == Keys.ENTER:
                self._output.draw_token(self._current_col, -1, GameToken.EMPTY)  # ← Ghost löschen
                return self._current_col

    def draw_board(self, board: list, state: GameState) -> None:
        # YOUR CODE HERE
        # TODO: draw grid with tokens using self._output
        # 1. Clear or reset cursor if necessary
        # 2. Iterate through the board 2D list
        self._output.draw_grid()  # ← Gitter zuerst!
        for r in range(6):
            for c in range(7):
                self._output.draw_token(c, r, board[r][c])

        Ansi.gotoXY(1, 15)
        if state == GameState.TURN_RED:
            print("Current Turn: RED   ")
        elif state == GameState.TURN_YELLOW:
            print("Current Turn: YELLOW")
        


if __name__ == '__main__':
    # use the code below to test your implementation

    # creates an empty board
    board = [[GameToken.EMPTY for _ in range(7)] for _ in range(6)]
    
    # put some tokens at 'impossible' locations
    # note: board[row][column] 
    board[0][0] = GameToken.RED     # top left corner
    board[0][6] = GameToken.YELLOW  # top right corner
    board[4][3] = GameToken.RED     # 2nd but last row, middle position

    p = PlayerConsole(GameToken.YELLOW)  # this is the yellow player ('0')

    Ansi.clear_screen() # make sure terminal is 'clean'
    Ansi.reset()

    # draw board for the player yellow using console output (color text)
    # also tell the yellow player that it's yellow's turn
    p.draw_board(board, GameState.TURN_YELLOW)  
    # you should now see the board with the 3 'impossible' tokens
    
    # now let's ask yellow for their turn (using console input/ output)
    pos = p.play_turn()

    # first reset colors and move the cursor below the board
    Ansi.reset()
    Ansi.gotoXY(1, 20) # what's the position right under YOUR board?

    # print out the position for you to check if it's correct
    print(f"Position selected: {pos}")

    row = 5  # put yellow's token in to last row
    board[row][pos] = GameToken.YELLOW # put yellow's token on the board

    # now, after yellow has made their turn, redraw board for the *yellow*
    # player so they can see what has changed (using console input/ output)
    # also tell the *yellow* player that it's now reds's turn
    p.draw_board(board, GameState.TURN_RED)
    # ...
