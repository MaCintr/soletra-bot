import unicodedata

def remover_acentos(s):
    """Remove acentos de uma string sem alterar outros caracteres"""
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
    )

def filtrar_palavras(caracters):
    """
    Filtra palavras de no mínimo 4 letras que:
    - são formadas apenas por letras
    - contêm obrigatoriamente a primeira letra de 'caracters'
    - todas as letras estão na lista 'caracters'
    - comparações ignoram acentos
    """
    letra_obg = remover_acentos(caracters[0].lower())
    letras_validas = set(remover_acentos(c.lower()) for c in caracters)
    
    with open("wordlist.txt", "r", encoding="utf-8") as f:
        wordlist = f.read().splitlines()

    palavras_validas = []
    for palavra in wordlist:
        palavra_limpa = palavra.strip().lower()
        if 4 <= len(palavra_limpa):
            if palavra_limpa.isalpha():  # garante só letras
                palavra_sem_acentos = remover_acentos(palavra_limpa)
                if letra_obg in palavra_sem_acentos and all(l in letras_validas for l in palavra_sem_acentos):
                    palavras_validas.append(palavra_limpa)  # mantém acentos na palavra final

    return palavras_validas
