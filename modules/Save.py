import json
from templates.default_save import *


class Save:
    def __init__(self):
        self.save_name = 'save.json'
        self.file = self.load_file()

    def load_file(self):
        try:   
            with open(self.save_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return DEFAULT_SAVE
        
    def save_file(self, data):
        with open(self.save_name, 'w') as file:
            json.dump(data, file)