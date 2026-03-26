from ansi import Ansi
from game_token import GameToken
from output_base import OutputBase

class OutputConsole(OutputBase):
    VERTICAL_OFFSET = 2         # this is the row where the board starts
    STATUS_LINE_OFFSET = 18     # can print here w/o distroying board visuals 

    def __init__(self):
        Ansi.clear_screen()
        Ansi.reset()

    def draw_grid(self) -> None:
        # YOUR CODE HERE
        Ansi.reset()
        Ansi.gotoXY(1, self.VERTICAL_OFFSET)
      
        print("┌────┬────┬────┬────┬────┬────┬────┐")
        for _ in range(5):
            print("│    │    │    │    │    │    │    │")
            print("├────┼────┼────┼────┼────┼────┼────┤")
        print("│    │    │    │    │    │    │    │")
        print("└────┴────┴────┴────┴────┴────┴────┘")



    def draw_token(self, x: int, y: int, token: GameToken = GameToken.EMPTY) -> None:

        term_x = (x * 5) + 3        
        # Wenn y = -1 (Ghost Token über dem Feld), setzen wir es direkt über das Grid
        if y < 0:
            term_y = self.VERTICAL_OFFSET - 1
        else:
            term_y = (y * 2) + 1 + self.VERTICAL_OFFSET
            
        Ansi.gotoXY(term_x, term_y)
        
        # Die Farbe des Tokens abhängig vom Spieler wählen
        if token == GameToken.RED:
            Ansi.set_foreground(1, True)  # 1 = Rot
            print("██", end="", flush=True)
        elif token == GameToken.YELLOW:
            Ansi.set_foreground(3, True)  # 3 = Gelb
            print("██", end="", flush=True)
        else:
            Ansi.reset()
            print("  ", end="", flush=True) # Feld leeren
        
        Ansi.reset()


if __name__ == '__main__':
    # use the code below to test your implementation
    from input_console import InputConsole
    from input_base import Keys

    Ansi.clear_screen()
    Ansi.reset()

    oc = OutputConsole()
    row, col = 0, 0

    oc.draw_grid()
    oc.draw_token(col, row, GameToken.RED)

    Ansi.gotoXY(1, 16)
    
    print("Nutze Pfeiltasten zum Bewegen. ESC zum Beenden.")
    print("Falls Pfeiltasten nicht gehen: Starte das Skript in CMD/Terminal!")

    input_sys = InputConsole()
    while True:
        key = input_sys.read_key()
        
        # Alten Stein löschen
        oc.draw_token(col, row, GameToken.EMPTY)

        if key == Keys.RIGHT: col = (col + 1) % 7
        if key == Keys.LEFT:  col = (col - 1) % 7
        if key == Keys.DOWN:  row = (row + 1) % 6
        if key == Keys.UP:    row = (row - 1) % 6
        
        if key == Keys.ESC:
            Ansi.gotoXY(1, 20)
            print("Test beendet.")
            break

        # Neuen Stein zeichnen
        oc.draw_token(col, row, GameToken.RED)