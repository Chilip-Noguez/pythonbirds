class Pessoa:
    def __init__(self, *filhos, nome=None, idade=37):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    preta = Pessoa(nome='Preta N')
    pimenta = Pessoa(nome='Pimenta N')
    felipe = Pessoa(pimenta, preta, nome='Felipe')
    print(Pessoa.cumprimentar(felipe))
    print(id(felipe))
    print(felipe.cumprimentar())
    print(felipe.nome)
    print(felipe.idade)
    for filho in felipe.filhos:
        print(filho.nome)
    felipe.sobrenome = 'Noguez'
    print(felipe.sobrenome)
    print(felipe.__dict__)
    print(pimenta.__dict__)
    del felipe.filhos
    print(felipe.__dict__)
