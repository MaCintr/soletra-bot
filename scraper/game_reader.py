from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from scraper.browser import iniciar_browser
from solver.word_filter import filtrar_palavras

def ler_elementos_da_pagina():

    driver = iniciar_browser()    
    actions = ActionChains(driver)
    driver.get("https://g1.globo.com/jogos/soletra/")
    
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".button.button--game-white.intro-button.svelte-1t84pcu").click()
    print("---------------- Iniciando jogo ----------------")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".button.button--game-white.drawer-close-icon.svelte-1t84pcu").click()
    print("---------------- Fechando instruções ----------------")
    time.sleep(1)
    


    letra_obg_elemento = driver.find_element(By.CSS_SELECTOR, ".hexagon-cell.center.svelte-1vt3j7k")
    letras_elemento = driver.find_elements(By.CSS_SELECTOR, ".hexagon-cell.outer.svelte-1vt3j7k")

    letra_obg = letra_obg_elemento.text
    letras_fora = [el.text for el in letras_elemento]
    letras = [letra_obg] + letras_fora



    print("Letras encontradas => ", letras)
    
    palavras_validas = filtrar_palavras(letras)
    print(f"Palavras válidas para o desafio ({len(palavras_validas)})=> ", palavras_validas)
    
    actions.move_to_element(driver.find_element(By.TAG_NAME, "body")).click().perform()
    
    index = 1

    for palavra in palavras_validas:
        print(f"Testando palavra {index} de {len(palavras_validas)}=> ", palavra)
        index += 1
        for letra in palavra:
            actions.send_keys(letra).perform()
            time.sleep(0.1)
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(0.5)
    
    print("Lista de palavras percorrida com sucesso!")
    time.sleep(3)
    print("Encerrando partida")
    botao_encerrar = driver.find_element(By.CSS_SELECTOR, 'button[title="Botão responsável por encerrar o jogo"]')
    botao_encerrar.click()
    time.sleep(30)
    driver.quit()
