import reflex as rx


class State(rx.State):

    ## * Variables de estado para la UI
    left_open = True  
    right_open = True
    game_status = 'stopped'

    ## * Toggles para los diferentes estados de la UI

    def toggle_left(self):
        self.left_open = not self.left_open

    def toggle_right(self):
        self.right_open = not self.right_open
    
    # * Toggles para el estado de juego

    def start(self):
        self.game_status = 'playing'

    def pause(self):
        if self.game_status == 'playing':
            self.game_status = 'paused'

    def resume(self):
        if self.game_status == 'paused':
            self.game_status = 'playing'

    def stop(self):
        self.game_status = 'stopped'
