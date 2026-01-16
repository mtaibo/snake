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
        return rx.call_script('initGame("game-canvas")')

    def pause_resume(self):
        if self.game_status == 'playing':
            self.game_status = 'paused'
        elif self.game_status == 'paused':
            self.game_status = 'playing'

    def stop(self):
        self.game_status = 'stopped'


    ## ! KEY DOWN HANDLER

    def on_key_down(self, key: str, info: KeyInputInfo):
            # Ejemplo: pausar con Space, reset con R
            if key == " ":
                if self.game_status == 'playing':
                    self.game_status = 'paused'
                elif self.game_status == 'paused':
                    self.game_status = 'playing'
                elif self.game_status == 'stopped':
                    self.game_status = 'playing'

            if key.lower() == 'r':
                self.game_status = 'stopped'


class GameState(rx.State):

    running: bool = False