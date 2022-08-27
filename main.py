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


input = "\n\rASDF823gf \n\r\t  *\n\r\t   A\n\r\t   := \n\r\t  0\n\r\t  +\n\r\t  101\n\r\t  -\n\r\t  b9\n\r\t  *\n\r\t  1234\n\r\t  /\n\r\t  2\n\r\t  <\n\r\t  1\n\r\t  >\n\r\t  ==\n\r\t  asdf\n\r\t  "

tokens = Lexify(input)
Test(tokens)
