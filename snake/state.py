from reflex.event import KeyInputInfo
import reflex as rx
import enum

# Defined an enum object to manage game state
class GameStatus(str, enum.Enum):
    STOPPED = 'stopped'
    PLAYING = 'playing'
    PAUSED = 'paused'

class Direction(str, enum.Enum):
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'

# Main app state object
class State(rx.State):

    # State variables for sidebars
    left_sidebar_open: bool = False  
    right_sidebar_open: bool = False

    # State variable for game status
    game_status: GameStatus = GameStatus.STOPPED

    # Key handler function
    def on_key_down(self, key: str, info: KeyInputInfo):
            
            if key == ' ': return self.pause_resume() # Play/Pause key
            if key.upper() == 'R': return self.stop() # Restart key

            # Movement keys
            if self.game_status == GameStatus.PLAYING:
                if key == 'ArrowUp' or key.upper() == 'W':
                    return rx.call_script('changeDirection("UP")')
                elif key == 'ArrowDown' or key.upper() == 'S':
                    return rx.call_script('changeDirection("DOWN")')
                elif key == 'ArrowRight' or key.upper() == 'D':
                    return rx.call_script('changeDirection("RIGHT")')
                elif key == 'ArrowLeft' or key.upper() == 'A':
                    return rx.call_script('changeDirection("LEFT")')

    # Function to open or close sidebars
    def toggle_sidebar(self, side: str):
        if side == 'right': self.right_sidebar_open = not self.right_sidebar_open
        elif side == 'left': self.left_sidebar_open = not self.left_sidebar_open
    
    # Internal function to syncronize game_status on PY to gameStatus on JS
    def _sync_js_status(self):
        return rx.call_script(f'setGameStatus("{self.game_status.value}", "game-canvas")')

    ## FUNCTION GROUP TO CHANGE GAME_STATUS

    def start(self):
        self.game_status = GameStatus.PLAYING
        return self._sync_js_status()

    def stop(self):
        self.game_status = GameStatus.STOPPED
        return self._sync_js_status()

    def pause_resume(self):
        if self.game_status == GameStatus.PLAYING: self.game_status = GameStatus.PAUSED
        elif self.game_status == GameStatus.PAUSED: self.game_status = GameStatus.PLAYING
        return self._sync_js_status()
