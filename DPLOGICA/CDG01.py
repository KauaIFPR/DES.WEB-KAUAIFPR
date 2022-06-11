
#O Codigo Ira receber 5 números do usuario.
N1 = int(input("Diga seu Primeiro número inteiro?"))
N2 = int(input("Diga seu Segundo número inteiro?"))
N3 = int(input("Diga seu Terceiro número inteiro?"))
N4 = int(input("Diga seu Quarto número inteiro?"))
N5 = int(input("Diga seu Quinto número inteiro?"))

#O Codigo ira encontrar o maior número dentre os cinco, e então ira mostrar na tela do usuario!

if N1 > N2 and N1 > N3 and N1 > N4 and N1 > N5:
    print("O Maior número dentre os 5 é", N1)
elif N2 > N1 and N2 > N3 and N2 > N4 and N2 > N5:
    print("O Maior numero dentre os 5 é", N2)
elif N3 > N2 and N3 > N1 and N3 > N4 and N3 > N5:
    print("O Maior número dentre os 5 é", N3)
elif N4 > N2 and N4 > N1 and N4 > N3 and N4 > N5:
    print("O maior número dentre os 5 é", N4)
elif N5 > N2 and N5 > N1 and N5 > N4 and N5 > N3:
    print("O maior número dentre os 5 é", N5)

#FIM CODIGO