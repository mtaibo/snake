import readchar
import re
import os

class Menu():

    def __init__(self) -> None:
        self.args = {}
        self.type = ''
        self.name = ''
        self.options = []
        self.template = ''

    def reload(self):
        self.template = ''
        for letter in self.args[1]['body']: 
            if letter == '[':
                self.type = 0 
                break
            else: self.type = 1
        if self.type == 0: self.options = re.findall(r'\[(\w)\]', self.args[1]['body'])
        hyphen = '-' * len(self.args[1]['head'])
        self.template += '{}\n{}\n{}'.format(hyphen, self.args[1]['head'], hyphen)
        self.template += '\n\n{}\n\n: '.format(self.args[1]['body'])
    
    def convert(self, args):
        
        lines = args.splitlines()

        head = lines.copy()
        for n in head:
            if n == '': head.remove(n)
            elif n == '-' * len(lines[1]):
                head = head[1]
                break

        body = lines.copy()
        body_string = ''
        del body[0:5]
        for n in range(0,len(body)):
            if body[n] == ': ': break
            elif body[n] == '' and body[n+1] == ': ' or body[n+1] == ':': break
            elif body[n] != '' and body[n+1] != '': body_string += f'{body[n]}\n'
            elif body[n] != '' and body[n+1] == '': body_string += f'{body[n]}\n\n'
            elif body[n] == '': continue
        body = body_string.rstrip('\n')

        self.args = [self.type, {'head': head, 'body': body}]

    def deploy(self, args):
        self.convert(args)
        self.reload()

        while True:
            os.system('clear')
            print(self.template, end='')

            if self.type == 0:
                self.input = readchar.readchar()
                if self.input.upper() not in self.options: continue
                else: break

            elif self.type == 1:
                self.input = input()
                break