#O codigo ira pedir 10 numeros inteiros do usuario!!
N1 = int(input("Diga seu Primeiro número inteiro?"))
N2 = int(input("Diga seu Segundo número inteiro?"))
N3 = int(input("Diga seu Terceiro número inteiro?"))
N4 = int(input("Diga seu Quarto número inteiro?"))
N5 = int(input("Diga seu Quinto número inteiro?"))
N6 = int(input("Diga seu Sexto número inteiro?"))
N7 = int(input("Diga seu Sétimo número inteiro?"))
N8 = int(input("Diga seu Oitavo número inteiro?"))
N9 = int(input("Diga seu Nono número inteiro?"))
N10 = int(input("Diga seu Décimo número inteiro?"))

#Ira fazer a divisão por 2 com todos os numeros!
#Se for par sempre sera 0 e se for impar sera 1
resu01 = N1 % 2
resu02 = N2 % 2
resu03 = N3 % 2
resu04 = N4 % 2
resu05 = N5 % 2
resu06 = N6 % 2
resu07 = N7 % 2
resu08 = N8 % 2
resu09 = N9 % 2
resu10 = N10 % 2

#Esta parte do codigo ele esta conferindo se o numero dito pelo usuario e dividido por 2 deu o valor igual a 0 ou 1
#Tivemos a utilização do SE SIM e SE NÂO, se caso o numero der 0 diga PAR e se der 1 diga IMPAR
if resu01 == 0:
    print("O número {} é PAR".format(N1))
else:
    print("O número {} é IMPAR".format(N1))
if resu02 == 0:
    print("O número {} é PAR".format(N2))
else:
    print("O número {} é IMPAR".format(N2))
if resu03 == 0:
    print("O número {} é PAR".format(N3))
else:
    print("O número {} é IMPAR".format(N3))
if resu04 == 0:
    print("O número {} é PAR".format(N4))
else:
    print("O número {} é IMPAR".format(N4))
if resu05 == 0:
    print("O número {} é PAR".format(N5))
else:
    print("O número {} é IMPAR".format(N5))
if resu06 == 0:
    print("O número {} é PAR".format(N6))
else:
    print("O número {} é IMPAR".format(N6))
if resu07 == 0:
    print("O número {} é PAR".format(N7))
else:
    print("O número {} é IMPAR".format(N7))
if resu08 == 0:
    print("O número {} é PAR".format(N8))
else:
    print("O número {} é IMPAR".format(N8))
if resu09 == 0:
    print("O número {} é PAR".format(N9))
else:
    print("O número {} é IMPAR".format(N9))
if resu10 == 0:
    print("O número {} é PAR".format(N10))
else:
    print("O número {} é IMPAR".format(N10))

#FIM CODIGO