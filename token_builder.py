from lexema_type import LexemaTypes
import re


class Token:
    def __init__(self, string):
        self.tokenize(string)

    def tokenize(self, string):
        for lexema_type in LexemaTypes:
            match = re.match(lexema_type.value.regex, string)
            if match:
                self.lexema = match.string.lstrip()
                self.id = lexema_type.value.id
                self.name = lexema_type.name
                break

    def __repr__(self):
        return '({}, {}, {})'.format(self.name, self.lexema, self.id)
