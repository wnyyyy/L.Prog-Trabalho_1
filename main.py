from token_builder import Token

def getNextToken(string):
    token = Token(string)
    return token

def trimInput(string, token):
    length = len(token.lexema)
    string = string[length:]
    return string

test = ") *2"

tokens = []
finished = False
while not finished:
    token = getNextToken(test)
    test = trimInput(test, token)
    tokens.append(token)
