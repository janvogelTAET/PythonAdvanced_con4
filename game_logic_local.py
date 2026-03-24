from game_token import GameToken
from game_state import GameState
from drop_state import DropState
from game_logic_base import GameLogicBase


class GameLogicLocal(GameLogicBase):
    ROWS = 6
    COLS = 7

    def __init__(self):

        # YOUR CODE HERE
        pass


    def get_state(self) -> GameState:
        # retruns a GameState enumeration constant

        # YOUR CODE HERE        
        return ...


    def drop_token(self, player: GameToken, column: int) -> DropState:
        # returns a DropToken (DROP_OK, COLUMN_INVALID, COLUMN_FULL, WRONG_PLAYER)

        # YOUR CODE HERE        
        return ...