class Pessoa:
    def __init__(self, *filhos, nome=None, idade=37):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def comprimentar(self):
        return f"Olá {id(self)}"


if __name__ == '__main__':
    silvajr = Pessoa(nome='Silvajr')
    carlos = Pessoa(silvajr, nome='Carlos')
    print(Pessoa.comprimentar(carlos))
    print(id(carlos))
    print(carlos.comprimentar())
    print(carlos.nome)
    print(carlos.idade)
    for filho in carlos.filhos:
        print(filho.nome)

