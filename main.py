from token_builder import Token

## gera uma lista de token a partir de uma string de entrada e retorna essa lista
def Lexify(inputString):
    tokens = []
    while len(inputString) > 0:
        token = Token()
        # chama tokenize() com a string de entrada, preenche os dados do token e tem como retorno o tamanho do input utilizado
        # note que 'length' não é o tamanho exato do lexema, mas o tamanho dos dados interpretados pelo regex, ou seja "\n +" possui tamanho 4, não 1
        length = token.tokenize(inputString)
        # tokenize retorna False caso um token não seja encontrado, nesse caso, quebra o loop e para a análise
        if not length:
            break
        else:
            # corta parte da string referente ao que foi interpretado pelo regex
            inputString = inputString[length:]
            tokens.append(token)
    return tokens

## função de resposta do input
## conta quantos tokens tem, imprime a lista e reconstrói o input a partir da lista para verificar mais fácil
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