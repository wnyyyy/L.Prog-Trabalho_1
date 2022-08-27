from lexema_type import LexemaTypes
import re


class Token:

    def tokenize(self, string):
        for lexema_type in LexemaTypes:
            match = re.match(lexema_type.value.regex, string)
            if match:
                content = match.group(0)
                self.lexema = content.lstrip()
                self.id = lexema_type.value.id
                self.name = lexema_type.name
                return len(content)
        return False

    def __repr__(self):
        return '({}, \"{}\", {})'.format(self.name, self.lexema, self.id)
