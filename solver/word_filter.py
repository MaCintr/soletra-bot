import unicodedata

def remover_acentos(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
    )

def filtrar_palavras(caracters, limite):
    letra_obg = remover_acentos(caracters[0].lower())
    letras_validas = set(remover_acentos(c.lower()) for c in caracters)
    
    with open("wordlist.txt", "r", encoding="utf-8") as f:
        wordlist = f.read().splitlines()

    palavras_validas = []
    for palavra in wordlist:
        palavra_limpa = palavra.strip().lower()
        if 4 <= len(palavra_limpa) <= limite:
            if palavra_limpa.isalpha():
                palavra_sem_acentos = remover_acentos(palavra_limpa)
                if letra_obg in palavra_sem_acentos and all(l in letras_validas for l in palavra_sem_acentos) and (palavra_sem_acentos in palavras_validas) == False:
                    palavras_validas.append(palavra_sem_acentos)

    return sorted(palavras_validas, key=len)
