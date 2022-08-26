from enum import Enum


class Lexema(Enum):
    VAR = '\\b([a-zA-Z]{1}[0-9a-zA-Z_]{0,98})\\b.*'
    NUM = '\\b([1-9]\d{0,98})\\b.*'
    LPAR = '(\({1})'
    RPAR = '(\){1})'
    ADDOP = '(\+{1})'
    SUBOP = '(\-{1})'
    MULOP = '(\*{1})'
    DIVOP = '(\/{1})' 
    LTOP = '(\>{1})'
    STOP = '(\<{1})'
    EQOP = '(\={2})'
    ASSIGNOP = '(\:\={1})'