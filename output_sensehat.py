import time
from sense_hat import SenseHat
from game_token import GameToken
from output_base import OutputBase

class OutputSenseHat(OutputBase):
    """
    Handles the visual output for the Connect 4 game using the Raspberry Pi SenseHat LED matrix.
    """

    def __init__(self):
        self._sense = SenseHat()
        self._sense.clear()
        
        self._color_red = (255, 0, 0)
        self._color_yellow = (255, 255, 0)
        self._color_board = (0, 0, 255)
        self._color_empty = (0, 0, 0)

    def draw_grid(self) -> None:
        """
        Draws the initial empty game board on the SenseHat matrix.
        The board spans logical columns 0-6 and physical matrix rows 2-7.
        """
        self._sense.clear()
        for col in range(7):
            for row in range(6):
                self._sense.set_pixel(col, row + 2, self._color_board)

    def draw_token(self, x: int, y: int, token: GameToken = GameToken.EMPTY) -> None:
        """
        Draws a specific game token at the given logical game coordinates.
        Maps logical coordinates (y: -1 to 5) to physical SenseHat coordinates (y: 1 to 7).
        """
        matrix_x = x
        matrix_y = y + 2
        
        color = self._color_empty
        
        if token == GameToken.RED:
            color = self._color_red
        elif token == GameToken.YELLOW:
            color = self._color_yellow
        elif token == GameToken.EMPTY:
            if y >= 0:
                color = self._color_board
            else:
                color = self._color_empty
                
        self._sense.set_pixel(matrix_x, matrix_y, color)

if __name__ == '__main__':
    # Test routine for standalone execution
    output = OutputSenseHat()
    output.draw_grid()
    
    # Test hovering token
    output.draw_token(3, -1, GameToken.YELLOW)
    time.sleep(1)
    output.draw_token(3, -1, GameToken.EMPTY)
    
    # Test placed tokens
    output.draw_token(0, 5, GameToken.YELLOW)
    output.draw_token(1, 5, GameToken.RED)
