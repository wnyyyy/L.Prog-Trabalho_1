from lexema_type import LexemaTypes
import re

## classe que representa um objeto do tipo token
class Token:

    ## preenche os dados do token e retorna informação necessária
    def tokenize(self, string):
        # loop que percorre cada constante declarada em LexemaTypes
        for lexema_type in LexemaTypes:
            # match em vez de search porque a busca deve ser obrigatoriamente no início da string, visto que queremos uma lista sequencial de tokens
            match = re.match(lexema_type.value.regex, string)
            if match:
                # em match.group(0) há o input da string que representa o lexema, pode incluir caracteres não relevantes
                # exemplo:  content pode ser "  \r\t abc" mas o lexema de fato é "abc"
                content = match.group(0)
                # corta os caracteres inúteis à esquerda para termos o lexema. Não é necessário cortar à direita, pois o regex já delimita
                self.lexema = content.lstrip()
                # id do token está armazenado no LexemaType dessa constante de LexemaTypes
                self.id = lexema_type.value.id
                # nome do token é o próprio nome do LexemaType
                self.name = lexema_type.name
                return len(content)
        # não foi encontrado um token, então retorna False. 
        # pode se dar tanto porque foi encontrado um caractere inválido ou porque só há espaços em branco ou afins no restante da string 
        return False

    def __repr__(self):
        return '({}, \"{}\", {})'.format(self.name, self.lexema, self.id)
