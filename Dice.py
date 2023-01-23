import random

def jogar_dado():
    
    rolar = input("Deseja jogar o dado? (Sim/Não): ")

    while rolar.lower() == "Sim".lower():
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)

        print("Dados rolados: {} e {} ".format(dado1, dado2))

        rolar = input("Rolar denovo? (S/N): ")

jogar_dado()