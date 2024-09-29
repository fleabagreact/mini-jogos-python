import random
from src.palavras import palavras_dicionario
from src.validacoes import validar_entrada, verificar_vitoria
from src.desenho import desenhar_boneco

def jogar_forca():
    palavras = []
    for categoria, lista_palavras in palavras_dicionario.items():
        palavras.extend(lista_palavras)
    
    palavra_secreta = random.choice(palavras)
    letras_descobertas = ['_' for _ in palavra_secreta]
    tentativas = 6
    letras_erradas = []

    print('Bem-vindo ao jogo da forca!')
    print(f'A palavra possui {len(palavra_secreta)} letras.')

    while tentativas > 0:
        desenhar_boneco(tentativas)
        print("\nPalavra atual: ", ' '.join(letras_descobertas))
        print("Letras erradas: ", ' '.join(letras_erradas))
        print("Tentativas restantes:", tentativas)

        letra = input("\nDigite uma letra: ").lower()

        if not validar_entrada(letra, letras_descobertas, letras_erradas):
            continue

        if letra in palavra_secreta:
            for i, l in enumerate(palavra_secreta):
                if l == letra:
                    letras_descobertas[i] = letra
            print(f"Você acertou a letra '{letra}'!")
        else:
            tentativas -= 1
            letras_erradas.append(letra)
            print(f"Você errou! A letra '{letra}' não está na palavra.")

        if verificar_vitoria(letras_descobertas):
            desenhar_boneco(tentativas)
            print("\nParabéns! Você ganhou!")
            print(f"A palavra era: {palavra_secreta}")
            break

    if tentativas == 0:
        desenhar_boneco(tentativas)
        print("\nVocê perdeu! A palavra era:", palavra_secreta)