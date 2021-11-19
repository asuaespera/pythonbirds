class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=37):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def comprimentar(self):
        return f"Olá {id(self)}"

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos{cls.olhos}'

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
    carlos.sobrenome = 'Alberto'
    del carlos.filhos
    carlos.olhos = 1
    del carlos.olhos
    print(carlos.__dict__)
    print(silvajr.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(carlos.olhos)
    print(silvajr.olhos)
    print(id(Pessoa.olhos), id(carlos.olhos), id(silvajr.olhos))
    print(Pessoa.metodo_estatico(), carlos.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), carlos.nome_e_atributos_de_classe())