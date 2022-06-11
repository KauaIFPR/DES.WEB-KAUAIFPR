#Aqui o codigo esta criando um esquema de loop infinito, aonde ao terminar sempre voltara ao começo!!
while True:
#Esta parte o codigo esta pergunto ao usuario qual a tabuada que ele deseja pesquisar!!
    n = int(input("Diga qual tabuada você deseja?"))
#Esta parte do codigo o mesmo ira montar a tabuada do numero desejado pelo usuario!
    print('-' * 30)
    for c in range(1, 11):
        print("{} x {} = {}".format(n, c, n*c))
    print('-' * 30)
#Como dito ao termino da tabuada pedida pelo usuario o codigo ira voltar a pedir qual o numero de tabuada que ele deseja!
    print("PROGRAMA DA TABUADA ENCERRADO.. VOLTE SEMPRE!!")

#FIM CODIGO