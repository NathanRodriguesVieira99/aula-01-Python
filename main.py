print('Hello World')
print('=========================')

arr = ['Egito', 'Grécia', 'Palestina', 'Pérsia']
print(arr)


print('=========================')

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        return f"Olá, meu nome é {self.nome}"


pessoa1 = Pessoa("Nathan", 19)
pessoa2 = Pessoa("VH", 21)

print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa1.falar())

print('=========================')

print(pessoa2.nome)
print(pessoa2.idade)
print(pessoa2.falar())
