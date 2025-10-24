from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from scraper.browser import iniciar_browser
from solver.word_filter import filtrar_palavras

def ler_elementos_da_pagina():
    
    # Coletar o tamanho da maior palavra do desafio para limitar o tamanho das palavras no filtro
    def coletar_limite():
        tamanho_palavras = driver.find_elements(By.CSS_SELECTOR, ".word-box.svelte-9jj3fa")

        ultimo_elemento = tamanho_palavras[-1]

        texto_ultimo_elemento = ultimo_elemento.text.strip()
        print("Limite => ", texto_ultimo_elemento)

        limite = int(texto_ultimo_elemento[:2])
        
        return limite

    driver = iniciar_browser()    
    actions = ActionChains(driver)
    driver.get("https://g1.globo.com/jogos/soletra/")
    
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".button.button--game-white.intro-button.svelte-1t84pcu").click()
    print("---------------- Iniciando jogo ----------------")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".button.button--game-white.drawer-close-icon.svelte-1t84pcu").click()
    print("------------- Fechando instruções --------------")
    time.sleep(1)
    


    letra_obg_elemento = driver.find_element(By.CSS_SELECTOR, ".hexagon-cell.center.svelte-1vt3j7k")
    letras_elemento = driver.find_elements(By.CSS_SELECTOR, ".hexagon-cell.outer.svelte-1vt3j7k")

    letra_obg = letra_obg_elemento.text
    letras_fora = [el.text for el in letras_elemento]
    letras = [letra_obg] + letras_fora



    print("Letras encontradas => ", letras)
    
    palavras_validas = filtrar_palavras(caracters=letras, limite=coletar_limite())
    print(f"Palavras válidas para o desafio ({len(palavras_validas)})=> ", palavras_validas)
    
    actions.move_to_element(driver.find_element(By.TAG_NAME, "body")).click().perform()
    time.sleep(1)
    

    
    
    index = 1

    for palavra in palavras_validas:
        print(f"Testando palavra {index} de {len(palavras_validas)} => ", palavra)
        actions.move_to_element(driver.find_element(By.TAG_NAME, "body")).click().perform()
        time.sleep(0.2)
        index += 1
        for letra in palavra:
            actions.send_keys(letra).perform()
        actions.send_keys(Keys.ENTER).perform()
        elemento_acertos = driver.find_element(By.CSS_SELECTOR, ".points.svelte-9jj3fa")
        acertos = elemento_acertos.text.split("/")
        time.sleep(0.3)
        if acertos[0] == acertos[1]:
            print("Todas as palavras foram encontradas!")
            break
    
    elemento_acertos = driver.find_element(By.CSS_SELECTOR, ".points.svelte-9jj3fa")
    acertos = elemento_acertos.text.split("/")
    if acertos[0] == acertos[1]:
        pass
    else:
        print("Lista de palavras percorrida com sucesso!")
        time.sleep(3)
        print("-------------- Encerrando partida --------------")
        botao_encerrar = driver.find_element(By.CSS_SELECTOR, 'button[title="Botão responsável por encerrar o jogo"]')
        botao_encerrar.click()
        
    input("Jogo finalizado! Pressione Enter para fechar o navegador...")
    driver.quit()
