import random
import time
from os import system as sys; sys('cls')

#listas para jogo
baralho = ["Ás", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Valete", "Dama", "Rei"]
mão = []
dealer = random.randint(17, 21)

#intro
while True:
   print("Bem vindo ao Blackjack do Cabs!\n-não é 100% fiel ao de cassino\n")
   print("As regras são simples:")
   print("1- As cartas que você tirar, serão somadas.")
   print("2- Seu objetivo é ter um resultado maior que\no dealer.")
   print("3- Caso atinja 21, voê fez um blackjack, mas\nse passar, estourou.")
   print("4- S ou s para 'sim', N ou n para 'não'.")
   print("5- Seja paciente, algumas interações duram\n entre 2 e 4 segundos.\n")
   print("Valores: \nÁs = 1 ou 11\nDama, Valete e Rei = 10\n")
   continuar = input("pressione enter para continuar. ")
   sys('cls')
   if continuar == "":
      break
   else:
      break

#jogo
while True:
    if sum(mão) > 21:
       break
    elif sum(mão) == 21:
       break
    print(f"Em mãos: {sum(mão)}")
    escolha = input("Deseja pegar uma carta?\n")
    if escolha == "S" or escolha == "s":
        carta = random.choice(baralho)
        print(f"Você pegou {carta}")

        while True:
          if carta == baralho[0]:
            As = int(input("Você pegou Ás, escolha o valor de 1 ou 11 para atribuir:\n"))
            if As == 1:
                carta = 1
                break
            elif As == 11:
                carta = 11
                break
            else:
                print("Valor inválido, insira novamente")
                continue
          else:
              break
          
        while True:
          if carta == "Valete" or carta == "Dama" or carta == "Rei":
            carta = 10
            break
          else:
            break

        mão.append(carta)
        time.sleep(2)
        sys('cls')

    elif escolha == "N" or escolha == "n":
        sys('cls')
        break
    else:
        print("Resposta inválida")
        time.sleep(2)
        sys('cls')

#conclusão
print(f"Em sua mão:{sum(mão)}")
print(f"Nas mãos do dealer: {dealer}\n")

if sum(mão) > 21:
   print("Puts! Você estourou, mais cuidado na próxima!\n")
   print("Obrigado por jogar! ;)")
   exit()
elif sum(mão) == 21:
   print("Parabéns! Você fez um blackjack B)\n")
   print("Obrigado por jogar! ;)")
   exit()

if sum(mão) > dealer:
   print("Parabéns!! Você ganhou do dealer.")
elif sum(mão) < dealer:
   print("O dealer ganhou de você.")
else:
   print("foi um empate!")

print("\nObrigado por jogar! ;)")


