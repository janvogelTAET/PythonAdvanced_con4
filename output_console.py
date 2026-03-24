from ansi import Ansi
from game_token import GameToken
from output_base import OutputBase


class OutputConsole(OutputBase):
    VERTICAL_OFFSET = 2         # this is the row where the board starts
    STATUS_LINE_OFFSET = 15     # can print here w/o distroying board visuals 

    def __init__(self):
        Ansi.clear_screen()
        Ansi.reset()

    def draw_grid(self) -> None:
        # YOUR CODE HERE
        Ansi.reset()
        print(
"""
┌
┐
└
┘
├
┤
┼
─
│
┬
┴
█ 

https://de.wikipedia.org/wiki/Unicodeblock_Rahmenzeichnung
""")


    def draw_token(self, x: int, y: int, token: GameToken = GameToken.EMPTY) -> None:
        # YOUR CODE HERE
        Ansi.gotoXY(1, 20)
        pass


if __name__ == '__main__':
    # use the code below to test your implementation

    # for testing only
    from input_console import InputConsole
    from input_base import Keys

    Ansi.clear_screen()
    Ansi.reset()

    oc = OutputConsole()
    row, col = 3, 3

    oc.draw_grid()                          # you should see only the grid now
    oc.draw_token(col, row, GameToken.RED)  # now there is a red token at 3,3

    Ansi.gotoXY(1,17); Ansi.clear_line()    # make sure to have 20 lines for the console
    print("If you have implmented OutputConsole correctly, you should be able ")
    print("to move a red token up and down and left and right through the ")
    print("board. Press ESC to quit.")

    # this is an extended test
    input = InputConsole()
    while True:

        key = input.read_key()

        Ansi.gotoXY(1,17); Ansi.clear_line()
        print(f"Key: {key}, Type: {type(key)}")
    
        oc.draw_token(col, row, GameToken.EMPTY)  # clear old token

        if key == Keys.RIGHT: col = (col + 1) % 7  # 7 columns in connect 4
        if key == Keys.LEFT:  col = (col - 1) % 7
        if key == Keys.DOWN:  row = (row + 1) % 6  # 6 rows in connect 4
        if key == Keys.UP:    row = (row - 1) % 6

        if key == Keys.ENTER: row, col = 0, 0  # jump to top left position
        
        if (key == Keys.ESC):  # Abort with ESC
            print("Aborted on use request.")
            break

        oc.draw_token(col, row, GameToken.RED)  # draw new token
