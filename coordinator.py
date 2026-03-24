
from game_token import GameToken
from game_state import GameState
from drop_state import DropState
from player_base import PlayerBase
from game_logic_base import GameLogicBase 

class Coordinator:
    """
    The Coordinator mediates between one or two player objects (subclasses
    of PlayerBase) and the game logic (a subclass of GameLogicBase). The
    easiest case is a local game of two players, e.g., 2 objects of
    PlayerConsole and a GameLogicLocal object.
    """

    def __init__(self, game_logic: GameLogicBase, player_red: PlayerBase, player_yellow : PlayerBase):
        """
        Create a Coordinator that mediates between the game_logic and the
        players player_red and player_yellow, which are passed as arguments. 
        """
        
        self._game_logic = game_logic  # either GameLogicLocal or GameLogicClient
        # YOUR CODE HERE
        # ...


    def run(self):

        # play game until won or draw
        while (True):

            # YOUR CODE HERE
            # forever
            # - get game state from logic
            state = self._game_logic.get_state()
            # - if game over: end game
            # - get board from logic
            # - draw the board for the current player: current_player.draw_board(board, state)
            # - ask the current player for their turn: column = current_player.play_turn()
            # - tell the game logic to execute that move: self._game_logic.drop_token( player, column )
            # repeat
            #
            # NOTE: Even though a DropState enum exists, it is NOT required act on it!
            # Because if the drop does not succeed, the game state (in the game logic)
            # does not change und thus the same player will be again asked to make a
            # turn until it does succeed.


# start a local game
if __name__ == '__main__':
    print("Welcome to  Connect 4")

    # create the appropriate player and game logic objects
    game_logic = ...    # ADD YOUR CODE HERE instead of ...
    player_red = ...    # ADD YOUR CODE HERE instead of ...
    player_yellow = ... # ADD YOUR CODE HERE instead of ...

    coordinator = Coordinator(game_logic, player_red, player_yellow)
    coordinator.run() # start game
