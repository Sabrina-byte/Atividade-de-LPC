# ETE PORTO DIGITAL
# LPC - Introdução a Python
# Prof. Cloves Rocha
# Estudante: Sabrina Ferreira Pessoa da Cruz
# Turma: 1 Ano C

print ('Olá Mundo! Eu sou bot e meu nome é XF.')
print ('Você poderia me dar um número?')
numero = int(input(f'Digite aqui: '))
if numero % 2 == 0:
    print (f'Oh legal, o número informado foi {numero}, então ele é par.')
else:
    print (f'Oh legal, o número informado foi {numero}, então ele é impar.')

print ('Você pode agora me dar dois números?')
numbr = int(input('Coloque um aqui: '))
numbe = int(input('E outro aqui: '))
soma = numbr + numbe
print (f'Eu somei e deu isso {soma}, legal né?')

print ('Que tal agora você me dar as notas das suas atividades desse bimestre?')
no1 = int(input('A primeira aqui: '))
no2 = int(input('A segunda aqui: '))
no3 = int(input('Agora a terceira: '))
no4 = int(input('E agora a quarta: '))
no = no1 + no2 + no3 + no4
nota = no / 2
if nota >= 6:
    print (f'Você tirou {nota}, então você passou nessa unidade! Parabêns!')
else:
    print (f'Você tirou {nota} então precisa estudar mais e terá que fazer a recuperação da unidade')

print ('Não seria legal se eu pudesse também converter metros para centímetros, né?')
print ('Adivinha!')
print ('Eu posso!')
print ('Me de um valor em metros e eu o colocarei em centímetros.')
h = int(input('Coloque o valor aqui: '))
som = h / 100
print (f'Esse valor fica assim em centímetros {som} cm.')

print ('Eu adoro brincar com números e fazer cálculos.')
print ('Vamos calcular a área de um círculo e de um quadrado, vai ser divertido. Vamos começar com o círculo.')
raio = int(input('Coloque o raio aqui e eu direi a área do círculo: '))
soms = raio **2*3.14
print (f'{soms} essa é a área do seu círculo.')

print ('Agora a área do quadrado.')
ladqua = int(input('Coloque aqui o valor dos lados do quadrado: '))
are = laqua**2
print (f'A área do seu quadrado é essa {are}.')

print ('Mas olha que legal!')
arequad = are * 2
print (f'Eu multipliquei o resultado por dois e deu {arequad}, acho que ficou melhor assim ¯\_(ツ)_/¯.')
print ('Sabe se você me disser quanto ganha por hora e quantas horas trabalha eu posso advinhar seu salário.')
pon = int(input(f'Quanto você ganha por hora?:'))
opn = int(input(f'E quantas horas você trabalha?:'))
pno = (pon * 8) * 22
print (f'Seu salário é R${pno}, maneiro.')

print ('Vamos voltar a brincar com números?')
qu = float(input(f'Me de um número e eu direi se ele é positivo ou negativo: '))
if qu > 0:
    print (f'Seu número é positivo.')
else:
    print (f'Seu número é negativo.')
print ('Você poderia me dizer seu sexo?')
rs = str(input(f'Coloque F-Feminino e M-Masculino: '))
if rs == 'f':
    print ('Então você é um ser humano do sexo feminino.')
elif rs == 'm':
    print ('Então você é um ser humano do sexo Masculino.')
else:
    print ('Sexo ínvalido, erro de digitação?')

print ('Agora que tal brincarmos com letras, talvez as pessoas de humanas tenham ficado confusas até aqui.')
let = str(input(f'Me de uma letra e lhe direi se ela é uma vogal ou consoante:'))
if let == 'a e i o u':
    print ('Isso é uma vogal.')
else:
    print ('Isto é uma consoante.')
