from game_logic_local import GameLogicBase
from game_state import GameState
from game_token import GameToken
from drop_state import DropState
import requests

class GameLogicClient(GameLogicBase):
    """
    This class implements a GameLogic by delegating all method calls via REST
    to a server (game_logic_server.py). The server in turn delegates the calls
    to a GameLogicLocal object (which is local to the server).

    So the job of this class is to implement the three methods specified in
    GameLogicBase, that is, get_board(), get_state() and drop_token(). Each
    method then invokes the corresponding REST endpoint (which isimplemented
    by the server). It then unpacks the response, and returns the response 
    to the local caller.  
    """

    def __init__(self, host):
        super().__init__()
        print( f"GameLogicClient initialized with host {host}" )
        # use 127.0.0.1 if the server runs on the same machine as this code:
        # self._url = 'http://127.0.0.1:5000/api'
        self._url = f'http://{host}:5000/api'

    def get_board(self) -> list:
        # call remote endpoint /board
        response = requests.get( f"{self._url}/board")
        print(response)
        return response.json().get("board")

    def get_state(self) -> GameState:
        # call remote endpoint /state

        # YOUR CODE HERE
        return ...

    def drop_token(self, player, column) -> DropState:
        # call remote endpoint /drop

        # YOUR CODE HERE
        return ...

    def game_reset(self) -> None:
        # call remote endpoint  /reset

        # OPTIONAL: reset/ restart the game
        # YOUR CODE HERE
        pass

if __name__ == '__main__':
    """
    Test programm to manually check if GameLogicClient is working.
    
    NOTE: For the test to work, game_logic_server.py must be implemented and
    running.

    Limitations:
    - Mocks both players (at once):
      - no distributed gameplay possible
      - this is not a replacement for the Coordinator
    - Does not handle errors
    - Does not handle end of game gracefully
    """

    # local function
    def draw_board( board: list, state: GameState) -> None:
        print("0|1|2|3|4|5|6")
        for idx, row in enumerate(board):
            print('|'.join(row))
        print( f"GameState: {state}" )

    client = GameLogicClient()
    while( True ):
        game_state = client.get_state()
        board = client.get_board()

        draw_board( board, game_state )

        if game_state == GameState.TURN_RED or  game_state == GameState.TURN_YELLOW:
            player = GameToken.RED if game_state == GameState.TURN_RED else GameToken.YELLOW  
            column = int(input("Which colum to drop? "))    
            drop_state = client.drop_token( player, column )
            print( "drop_state:", drop_state )
        else: break # bail out if its neither RED's nor YELLOW's turn, i.e. WON or DRAW
    
    print("Game Over")
    # client.game_reset()  # call reset to restart the game logic in the server
