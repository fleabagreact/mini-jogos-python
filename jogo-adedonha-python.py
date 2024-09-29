import time
import random

def jogar_adedonha():
    rodadas = 3
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letras_usadas = []
    pontuacao = 0

    print("Bem-vindo ao jogo de Adedonha!")
    print("Regras:")
    print("1. Você tem 10 segundos para digitar uma palavra que comece com a letra da rodada.")
    print("2. Pontuação: Cada palavra válida dá 1 ponto.")
    print("3. Se o tempo se esgotar ou a palavra estiver errada, você não pontua naquela rodada.\n")
    
    nome_jogador = input("Digite seu nome: ")

    for rodada in range(1, rodadas + 1):
        # Escolhendo uma letra que ainda não foi usada
        letra = random.choice([l for l in letras if l not in letras_usadas])
        letras_usadas.append(letra)

        print(f"\nRodada {rodada}: A palavra deve começar com a letra '{letra}'.")

        # Controlando o tempo
        tempo_inicial = time.time()
        palavra = input("Digite uma palavra: ").upper()

        tempo_decorrido = time.time() - tempo_inicial

        if not palavra:
            print("Você não digitou nenhuma palavra!")
            continue

        if tempo_decorrido > 10:
            print("Tempo esgotado!")
            continue

        if palavra[0] != letra:
            print(f"A palavra '{palavra}' não começa com a letra '{letra}'!")
            continue
        
        # Palavra válida
        print(f"Palavra '{palavra}' aceita!")
        pontuacao += 1

    # Fim do jogo
    print(f"\nO jogo acabou! Sua pontuação final foi {pontuacao} pontos.")
    if pontuacao == rodadas:
        print(f"Parabéns {nome_jogador}! Você acertou todas as rodadas!")
    else:
        print(f"Boa tentativa {nome_jogador}! Tente novamente para melhorar sua pontuação.")

# Executa o jogo
jogar_adedonha()