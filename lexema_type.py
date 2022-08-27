from enum import Enum


class LexemaType:
    def __init__(self, regex, id):
        self.regex = regex
        self.id = id

class LexemaTypes(Enum):
    VAR = LexemaType(
        regex = r'\s*[a-zA-Z]{1}[0-9a-zA-Z_]{0,98}',
        id = 1)
    NUM = LexemaType(
        regex = r'\s*(0{1}|[1-9]\d{0,98})',
        id = 2)
    LPAR = LexemaType(
        regex = r'\s*\({1}',
        id = 3)
    RPAR = LexemaType(
        regex = r'\s*\){1}',
        id = 4)
    ADDOP = LexemaType(
        regex = r'\s*\+{1}',
        id = 5)
    SUBOP = LexemaType(
        regex = r'\s*\-{1}',
        id = 6)
    MULOP = LexemaType(
        regex = r'\s*\*{1}',
        id = 7)
    DIVOP = LexemaType(
        regex = r'\s*\/{1}',
        id = 8)
    LTOP = LexemaType(
        regex = r'\s*\>{1}',
        id = 9)
    STOP = LexemaType(
        regex = r'\s*\<{1}',
        id = 10)
    EQOP = LexemaType(
        regex = r'\s*\={2}',
        id = 11)
    ASSIGNOP = LexemaType(
        regex = r'\s*(\:\={1})',
        id = 12)
