# Simples, Composto ou Encadeado

n1 = n2 = 0.0

media = 0.0

n1 = float(input('Digite a nota: '))
n2 = float(input('Digite a nota: '))

media = (n1 + n2) / 2

if (media >= 7):
    print("Resultado: Aprovado")
    print("Parabéns")
elif (media >= 5):
    print('Recuperação!')
else:
    print('Aluno reprovado...')

print('Sua média é {}'.format(media))
