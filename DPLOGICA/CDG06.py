resposta = 'S'
soma = quant = maior = menor = 0
#O codigo ira pedir ao usuario um numero!
#Logo apos isso ira pedir novamente se o usuario ira querer colocar mais algum numero!
while resposta in 'Ss':
    NM = int(input("Digite seu número:"))
#Ira somar todos os valores ditos pelo usuario!
#E a quantidade de numeros inseridos!
    soma += NM
    quant += 1
#Utilizando SE SIM e SE NÂO fizemos que todos os numeros sejam separados em qual sera o maior e qual sera o menor!
    if quant == 1:
        maior = menor = NM
    else:
       if maior < NM:
         maior = NM
       if menor > NM:
          menor = NM
#O codigo ira pedir ao usuario se deseja colocar mais algum numero em seu codigo!
#Se caso ele quiser colocar apenas digite S se não N.
#N faz com que o codigo trabalhe somente com os numeros dito pelo usuario e não volte a perguntar se deseja colocar outro numero
    resposta = str(input("Deseja Continuar? [S/N] ")).upper().strip()[0]
#Aqui seria a resposta do codigo para o usuario aonde ira dizer a quantidade de numeros digitados e a soma deles!
print("Você Digitou {} números e a soma deles foi {}".format(quant, soma))
#E aqui qual numero é maior e qual seria o menor dentre todos os numeros digitados!
print("O Maior valor foi {} e o menor foi {}".format(maior, menor))

#FIM CODIGO