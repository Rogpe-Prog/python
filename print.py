# Sintaxe:
# print(objetos, argumentos)

mensagem = 'Função print'
print(mensagem)
print('Aula de python')

nome = 'Aloha'
chanel = 'Treinamentos'
print(chanel, ' - ', nome)

name = input('digite seun nome: ')
print('Olá al' + name + '! Bem vindo!!!')

print('primeiro print')
print('outro print ', end='')
print('continua na mesma liha')

# String Format

nam = 'Maria'
idade = 30
msg_format = 'O nome dela é {0} e elá tem {1} anos'.format(nam, idade)
print(msg_format)


#Chama de F string
nomee = 'Aloha'
peso = 73.50
msg = f'Olá, meu nome é {nome} e tenho {peso}'
print(msg)