import biologia
import historia
import geografia
import time

print("***********************************")
print("*** Bem vindo ao tema da forca  ***")
print("***********************************")

print("Os Temas disponiveis para a forca são: ")
print("(1) GEOGRAFIA (2) HISTORIA (3) BIOLOGIA")

def jogar():
    print("******************************")

escolha = int(input("Diga o tema que deseja para a forca: "))

if escolha == 1:
    print("Tema da forca escolhido.")
    print("Carregando...")
    time.sleep(2)
    geografia.jogar()
elif escolha == 2:
    print("Tema da forca escolhido.")
    print("Carregando...")
    time.sleep(2)
    historia.jogar()
elif escolha == 3:
    print("Tema da forca escolhido.")
    print("Carregando...")
    time.sleep(2)
    biologia.jogar()
else:
  print("TEMA INVALIDO")

if(__name__ == "__main__"):
    jogar()