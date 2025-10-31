# Permite manipular caracteres
from unidecode import unidecode

def filtrar_palavras(caracters: list[str], limite: int) -> list[str]:
    letra_obg = caracters[0].lower()
    letras_validas = set(c.lower() for c in caracters)

    # Remove palavras compostas e acentos de todas as palavras da wordlist e armazena em uma variável
    with open("wordlist.txt", "r", encoding="utf-8") as lista:
        wordlist = [unidecode(palavra.strip().lower()) for palavra in lista if palavra.strip().isalpha()]

    # Filtra as palavras válidas usando list comprehension
    palavras_validas = [
        palavra for palavra in wordlist
        if 4 <= len(palavra) <= limite
        and letra_obg in palavra
        and all(l in letras_validas for l in palavra)
    ]

    return sorted(set(palavras_validas), key=len)
