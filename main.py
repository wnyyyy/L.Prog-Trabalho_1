from token_builder import Token


def Lexify(inputString):
    tokens = []
    while len(inputString) > 0:
        token = Token()
        length = token.tokenize(inputString)
        if not length:
            break        
        else:
            inputString = inputString[length:]
            tokens.append(token)
    return tokens

def Test(tokens):
    print(f'\nQuantidade de tokens: {len(tokens)}')
    print('\nLista de tokens: ')
    result = ''
    for token in tokens:
        print(token)
        result += token.lexema    
    print('\nInput reconstruído:')
    print(result)

while(True):
    print('\nDigite uma string de entrada:')
    entry = input()
    tokens = Lexify(entry)
    Test(tokens)