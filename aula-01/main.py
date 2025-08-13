print('Hello World')
print(666)
print(7.62)

print('=========================')

string = 'String'
number = 10

print("String:", string)
print("Number:", number)

print('=========================')

soma = 1 + 1
subtracao = 1 - 1
multiplicacao = 2 * 5
divisao = 10 / 2

print("Soma:", soma)
print("Subtracão:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)

print('=========================')
arr = ['Egito', 'Grécia', 'Palestina', 'Pérsia']
print('Array:', arr)


print('=========================')


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        return f"Olá, meu nome é {self.nome}"


pessoa = Pessoa("Nathan", 19)
print('Obeto:', pessoa)

print(pessoa.nome)
print(pessoa.idade)
print(pessoa.falar())

print('=========================')
