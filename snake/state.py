import reflex as rx
from reflex.event import KeyInputInfo

class State(rx.State):

    ## * Variables de estado para la UI
    left_open = False  
    right_open = False
    game_status = 'stopped'

    ## * Toggles para los diferentes estados de la UI

    def toggle_left(self):
        self.left_open = not self.left_open

    def toggle_right(self):
        self.right_open = not self.right_open
    
    # * Toggles para el estado de juego

    def start(self):
        self.game_status = 'playing'
        return rx.call_script(f'setGameStatus("{self.game_status}", "game-canvas")')

    def pause_resume(self):
        if self.game_status == 'playing':
            self.game_status = 'paused'
            return rx.call_script(f'setGameStatus("{self.game_status}", "game-canvas")')
        elif self.game_status == 'paused':
            self.game_status = 'playing'
            return rx.call_script(f'setGameStatus("{self.game_status}", "game-canvas")')

    def stop(self):
        self.game_status = 'stopped'
        return rx.call_script(f'setGameStatus("{self.game_status}", "game-canvas")')


    ## ! KEY DOWN HANDLER

    def on_key_down(self, key: str, info: KeyInputInfo):
            
            # Play/Pause key
            if key == " ":
                if self.game_status == 'playing':
                    self.game_status = 'paused'
                    return rx.call_script(f'setGameStatus("{self.game_status}", "game-canvas")')
                elif self.game_status == 'paused':
                    self.game_status = 'playing'
                    return rx.call_script(f'setGameStatus("{self.game_status}", "game-canvas")')
                elif self.game_status == 'stopped':
                    self.game_status = 'playing'
                    return rx.call_script(f'setGameStatus("{self.game_status}", "game-canvas")')

            # Restart key
            if key.upper() == 'R':
                self.game_status = 'stopped'
                return rx.call_script(f'setGameStatus("{self.game_status}", "game-canvas")')

            # Movement keys
            if key == 'ArrowUp' or key.upper() == 'W':
                return rx.call_script('changeDirection("UP")')
            elif key == 'ArrowDown' or key.upper() == 'S':
                return rx.call_script('changeDirection("DOWN")')
            elif key == 'ArrowRight' or key.upper() == 'D':
                return rx.call_script('changeDirection("RIGHT")')
            elif key == 'ArrowLeft' or key.upper() == 'A':
                return rx.call_script('changeDirection("LEFT")')
