from game_token import GameToken
from game_state import GameState
from drop_state import DropState
from game_logic_base import GameLogicBase

class GameLogicLocal(GameLogicBase):
    ROWS = 6
    COLS = 7

    def __init__(self):

        # YOUR CODE HERE
        # Initialize empty board (using None)
        self._board = [[None for _ in range(self.COLS)] for _ in range(self.ROWS)]
        self._current_state = GameState.TURN_RED

    def get_state(self) -> GameState:
        # retruns a GameState enumeration constant

        # YOUR CODE HERE  
        return self._current_state

    def get_board(self):
        # Additional helper method needed by the coordinator to draw the board
        return self._board

    def drop_token(self, player: GameToken, column: int) -> DropState:
        # returns a DropToken (DROP_OK, COLUMN_INVALID, COLUMN_FULL, WRONG_PLAYER)

        # YOUR CODE HERE        
        # 1. Check if the correct player is making a move
        expected_token = GameToken.RED if self._current_state == GameState.TURN_RED else GameToken.YELLOW
        if player != expected_token:
            return DropState.WRONG_PLAYER

        # 2. Check if column is within valid range
        if not (0 <= column < self.COLS):
            return DropState.COLUMN_INVALID

        # 3. Check if column is full (check top row)
        if self._board[0][column] is not None:
            return DropState.COLUMN_FULL

        # 4. Drop the token (search from bottom to top)
        for row in reversed(range(self.ROWS)):
            if self._board[row][column] is None:
                self._board[row][column] = player
                break
        
        # 5. Update state (check for win / draw / next turn)
        self._update_game_state(player)
        
        return DropState.DROP_OK
    
    # --- Custom Helper Methods ---
    
    def _update_game_state(self, last_player: GameToken):
        # Update the game state based on the last move
        if self._check_win(last_player):
            self._current_state = GameState.WON_RED if last_player == GameToken.RED else GameState.WON_YELLOW
        elif self._is_board_full():
            self._current_state = GameState.DRAW
        else:
            self._current_state = GameState.TURN_YELLOW if last_player == GameToken.RED else GameState.TURN_RED

    def _is_board_full(self):
        # Check if the top row has any empty slots left
        return all(self._board[0][c] is not None for c in range(self.COLS))

    def _check_win(self, token: GameToken) -> bool:
        # Horizontal check
        for r in range(self.ROWS):
            for c in range(self.COLS - 3):
                if all(self._board[r][c+i] == token for i in range(4)): return True
        
        # Vertical check
        for r in range(self.ROWS - 3):
            for c in range(self.COLS):
                if all(self._board[r+i][c] == token for i in range(4)): return True
        
        # Diagonal check (bottom-left to top-right)
        for r in range(3, self.ROWS):
            for c in range(self.COLS - 3):
                if all(self._board[r-i][c+i] == token for i in range(4)): return True
                
        # Diagonal check (top-left to bottom-right)
        for r in range(self.ROWS - 3):
            for c in range(self.COLS - 3):
                if all(self._board[r+i][c+i] == token for i in range(4)): return True
                
        return False