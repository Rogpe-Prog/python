# lista = [2, 6, 9, 3, 7, 8, 10, 3, 4, 9, 7, 3]
# palavra = 'Aloha'

# for item in lista:
#     print(item)

# for letra in palavra:
#     print(letra)

# for numero in range(1, 11):
#     print(numero)

# nome = input('Digie seu nome: ')
# for x in range(10):
#     print(f'{x+1} {nome}')

# # range (valor_inicial, valor_final, incremento)
# for x in range(2, 20, 2):
#     print(x)

pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Safira', 'Diamante', 'Turmalina')

for pedra in pedras:
    if pedra == 'Quartzo':
        continue
    print(pedra)