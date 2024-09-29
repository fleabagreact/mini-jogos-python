import string

def validar_entrada(letra, letras_descobertas, letras_erradas):
    if len(letra) != 1:
        print('Entrada inválida! Digite apenas uma letra.')
        return False
    if letra not in string.ascii_lowercase:
        print('Entrada inválida! Digite apenas uma letra do alfabeto.')
        return False
    if letra in letras_descobertas or letra in letras_erradas:
        print('Você já tentou essa letra antes. Tente outra.')
        return False
    return True

def verificar_vitoria(letras_descobertas):
    return '_' not in letras_descobertas
