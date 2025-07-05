import json
from templates.default_save import *


class Save:
    def __init__(self):
        self.save_name = 'save.json'
        self.file = self.load_file()
        self.high_scores_format = ''
        self.load_formats()

    def load_file(self):
        try:   
            with open(self.save_name, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return DEFAULT_SAVE
        
    def save_file(self, data):
        with open(self.save_name, 'w') as file:
            json.dump(data, file)
    
    def load_formats(self):
        self.settings_format = list(self.file["settings"].values())

        max_name_length = 0
        for i in self.file['high_scores']:
            if len(i['name']) > max_name_length: max_name_length = len(i['name'])

        index = 1
        for i in self.file['high_scores']:
            self.high_scores_format += ('{} - {}{}---  {} \n'.format(
                index, i['name'], ' '*(max_name_length+2-len(i['name'])), i['score']))
            index += 1

