from enum import Enum

class Regexes(Enum):
    VAR = r'\s*[a-zA-Z]{1}[0-9a-zA-Z_]{0,98}'
    NUM = r'\s*[1-9]\d{0,98}'
    LPAR = r'\s*\({1}'
    RPAR = r'\s*\){1}'
    ADDOP = r'\s*\+{1}'
    SUBOP = r'\s*\-{1}'
    MULOP = r'\s*\*{1}'
    DIVOP = r'\s*\/{1}'
    LTOP = r'\s*\>{1}'
    STOP = r'\s*\<{1}'
    EQOP = r'\s*\={2}'
    ASSIGNOP = r'\s*\(\:={1})'

class LexemaType:
    def __init__(self, regex, id):
        self.regex = regex
        self.id = id

class LexemaTypes(Enum):
    VAR = LexemaType(Regexes.VAR.value, 1)
    NUM = LexemaType(Regexes.NUM.value, 2)
    LPAR = LexemaType(Regexes.LPAR.value, 3)
    RPAR = LexemaType(Regexes.RPAR.value, 4)
    ADDOP = LexemaType(Regexes.ADDOP.value, 5)
    SUBOP = LexemaType(Regexes.SUBOP.value, 6)
    MULOP = LexemaType(Regexes.MULOP.value, 7)
    DIVOP = LexemaType(Regexes.DIVOP.value, 8)
    LTOP = LexemaType(Regexes.LTOP.value, 9)
    STOP = LexemaType(Regexes.STOP.value, 10)
    EQOP = LexemaType(Regexes.EQOP.value, 11)
    ASSIGNOP = LexemaType(Regexes.ASSIGNOP.value, 12)
