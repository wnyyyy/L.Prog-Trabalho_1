class Token:
    def __init__(self, nome, lexema, id):
        self.nome = nome
        self.lexema = lexema
        self.id = id

    def __repr__(self):
        return '({}, {}, {})'.format(self.nome, self.lexema, self.id)
