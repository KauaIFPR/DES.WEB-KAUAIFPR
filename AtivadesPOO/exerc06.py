while True:
    n = int(input("Diga qual tabuada você deseja?"))
    print('-' * 30)
    for c in range(1, 11):
      print("{} x {} = {}".format(n, c, n * c))
    print('-' * 30)
    print("PROGRAMA DA TABUADA ENCERRADO.. VOLTE SEMPRE!!")