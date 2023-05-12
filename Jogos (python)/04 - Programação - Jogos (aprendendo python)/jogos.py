import forca
import adivinhacao


print("***********************************")
print("***Bem vindo! Escolha o seu jogo!**")
print("***********************************")

print("(1) Forca  (2) Adivinhacao")

jogo = int(input("Qual jogo? "))

if(jogo == 1):
    print("Jogando Forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogando Adivinhacao")
    adivinhacao.jogar()
