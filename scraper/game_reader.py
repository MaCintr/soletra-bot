from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from scraper.browser import iniciar_browser
from solver.word_filter import filtrar_palavras

numeros_validos = ['1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ', '10', '11', '12', '13', '14', '15']

def ler_elementos_da_pagina():
    
    # Coletar o tamanho da maior palavra do desafio para limitar o tamanho das palavras no filtro
    def coletar_limite():
        tamanho_palavras = driver.find_elements(By.CSS_SELECTOR, ".word-box.svelte-9jj3fa")
        ultimo_elemento = tamanho_palavras[-1].text.strip()
        limite = int(ultimo_elemento[:2])

        return limite

    def coletar_tamanho_minimo_das_palavras_faltantes():
        tamanho_palavras = driver.find_elements(By.CSS_SELECTOR, ".word-box.svelte-9jj3fa")
        tamanho_palavras_text = [item.text for item in tamanho_palavras]
        for item in tamanho_palavras_text:
            if item[:2] in numeros_validos:
                return int(item[:2])


    driver = iniciar_browser()    
    actions = ActionChains(driver)
    driver.get("https://g1.globo.com/jogos/soletra/")
    # time.sleep(3)
    
    
    try:
        btn_erro_ao_iniciar = driver.find_element(By.CSS_SELECTOR, ".button.button--primary.full-size-button.svelte-1t84pcu.full-width")
        print(btn_erro_ao_iniciar)
        btn_erro_ao_iniciar.click()
    except:
        pass

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button.button--game-white.intro-button.svelte-1t84pcu"))).click()
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
    time.sleep(1)
    
    botao_apagar = driver.find_element(By.CSS_SELECTOR, 'button[title="Botão responsável por apagar as letras que foram selecionadas"]')    
    
    index = 1
    
    iniciar_timer = time.perf_counter()

    for palavra in palavras_validas:
        acertos = driver.find_element(By.CSS_SELECTOR, ".points.svelte-9jj3fa").text.split("/")
        if acertos[0] == acertos[1]:
            print("Todas as palavras foram encontradas!")
            break
        # actions.move_to_element(driver.find_element(By.TAG_NAME, "body")).click().perform()
        # time.sleep(0.1)
        minimo = coletar_tamanho_minimo_das_palavras_faltantes()
        # print(minimo)
        if len(palavra) >= minimo:
            # time.sleep(0.05)
            print(f"Testando palavra {index} de {len(palavras_validas)} => ", palavra)
            
            actions.send_keys(palavra).perform()
            
            # time.sleep(0.05)
            actions.send_keys(Keys.ENTER).perform()
            # time.sleep(0.1)
            for letra in palavra:
                botao_apagar.click()
                time.sleep(0.02)
        else:
            print(f"Pulando palavra {index} de {len(palavras_validas)} => ", palavra)
        index += 1
    
    acertos = driver.find_element(By.CSS_SELECTOR, ".points.svelte-9jj3fa").text.split("/")
    if acertos[0] == acertos[1]:
        pass
    else:
        print("Lista de palavras percorrida com sucesso!")
        time.sleep(3)
        print("-------------- Encerrando partida --------------")
        botao_encerrar = driver.find_element(By.CSS_SELECTOR, 'button[title="Botão responsável por encerrar o jogo"]')
        botao_encerrar.click()
        
    finalizar_timer = time.perf_counter()
    tempo_de_exec = (finalizar_timer - iniciar_timer) / 60
    
    print("Jogo finalizado! Tempo de execução (em minutos) =>", tempo_de_exec)
    input("Pressione Enter para fechar o navegador...")
    driver.quit()
    
    