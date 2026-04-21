import sys
from game_token import GameToken
from game_state import GameState
from player_base import PlayerBase
from input_base import Keys
from util import Util
from ansi import Ansi

# Correct indentation for the conditional import
if Util.isRaspberry():
    from input_sensehat import InputSenseHat
    from output_sensehat import OutputSenseHat

class PlayerSenseHat(PlayerBase):
    def __init__(self, player: GameToken):
        # Correctly initialize the base class with the player token
        super().__init__(player)
        
        # Initialize SenseHat input and output
        self._output = OutputSenseHat() 
        self._input = InputSenseHat() 
        self._current_col = 3  # Start in the middle column for the 'ghost' token   

    def play_turn(self) -> int:
        # Draw the initial ghost token before the loop starts
        self._output.draw_token(self._current_col, -1, self._player)
        
        while True:
            key = self._input.read_key()

            if key == Keys.LEFT and self._current_col > 0:
                # Clear old position
                self._output.draw_token(self._current_col, -1, GameToken.EMPTY)
                self._current_col -= 1
                # Draw new position
                self._output.draw_token(self._current_col, -1, self._player)
                
            elif key == Keys.RIGHT and self._current_col < 6:
                # Clear old position
                self._output.draw_token(self._current_col, -1, GameToken.EMPTY)
                self._current_col += 1
                # Draw new position
                self._output.draw_token(self._current_col, -1, self._player)
                
            elif key == Keys.ENTER or key == Keys.DOWN: # Often SenseHat Joystick press is ENTER or DOWN
                # Clear ghost token when dropped
                self._output.draw_token(self._current_col, -1, GameToken.EMPTY)  
                return self._current_col

    def draw_board(self, board: list, state: GameState) -> None:
        # 1. Draw grid first!
        self._output.draw_grid()  
        
        # 2. Iterate through the board 2D list and draw tokens
        for r in range(6):
            for c in range(7):
                self._output.draw_token(c, r, board[r][c])

        # Print current turn to console (useful if monitoring via SSH/Terminal)
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
    board[0][0] = GameToken.RED     # top left corner
    board[0][6] = GameToken.YELLOW  # top right corner
    board[4][3] = GameToken.RED     # 2nd but last row, middle position

    # CHANGE: Test PlayerSenseHat instead of PlayerConsole
    p = PlayerSenseHat(GameToken.YELLOW)  # this is the yellow player

    Ansi.clear_screen() # make sure terminal is 'clean'
    Ansi.reset()

    # draw board for the player yellow 
    p.draw_board(board, GameState.TURN_YELLOW)  
    
    # ask yellow for their turn (using SenseHat input)
    pos = p.play_turn()

    # print out the position to console for you to check if it's correct
    Ansi.reset()
    Ansi.gotoXY(1, 20)
    print(f"Position selected: {pos}")

    row = 5  # put yellow's token in the last row
    board[row][pos] = GameToken.YELLOW # put yellow's token on the board

    # redraw board for the player so they can see what has changed
    p.draw_board(board, GameState.TURN_RED)