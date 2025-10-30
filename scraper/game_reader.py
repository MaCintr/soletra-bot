from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from scraper.browser import iniciar_browser
from solver.word_filter import filtrar_palavras

def ler_elementos_da_pagina():
    
    # Coletar o tamanho da maior palavra do desafio para limitar o tamanho das palavras no filtro
    def coletar_limite():
        tamanho_palavras = driver.find_elements(By.CSS_SELECTOR, ".word-box.svelte-9jj3fa")
        ultimo_elemento = tamanho_palavras[-1].text.strip()
        limite = int(ultimo_elemento[:2])

        return limite

    # Coletar o tamanho mínimo de palavras
    def coletar_tamanho_minimo_das_palavras_faltantes(palavra):
        lista = driver.find_elements(By.XPATH, f"//span[contains(., '{len(palavra)} letras')]")
        if len(lista) > 0:
            return True
        else:
            return False
            


    # Iniciar Browser
    driver = iniciar_browser()    
    driver.get("https://g1.globo.com/jogos/soletra/")
    
    # Verifica se dá erro ao iniciar
    try:
        btn_erro_ao_iniciar = driver.find_element(By.CSS_SELECTOR, ".button.button--primary.full-size-button.svelte-1t84pcu.full-width")
        print(btn_erro_ao_iniciar)
        btn_erro_ao_iniciar.click()
    except:
        pass

    # Clica no botão iniciar e fecha as instruções
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button.button--game-white.intro-button.svelte-1t84pcu"))).click()
    print("---------------- Iniciando jogo ----------------")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".button.button--game-white.drawer-close-icon.svelte-1t84pcu").click()
    print("------------- Fechando instruções --------------")
    time.sleep(1)
    

    # Coleta a letra obrigatódia (central) e as demais
    letra_obg_elemento = driver.find_element(By.CSS_SELECTOR, ".hexagon-cell.center.svelte-1vt3j7k")
    letras_elemento = driver.find_elements(By.CSS_SELECTOR, ".hexagon-cell.outer.svelte-1vt3j7k")
    letra_obg = letra_obg_elemento.text
    letras_fora = [el.text for el in letras_elemento]
    
    # Armazena as letras em um array, sendo a primeira letra é obrigatória
    letras = [letra_obg] + letras_fora



    print("Letras encontradas => ", letras)
    
    # Chama o método que filtra apenas palavras que podem ser inseridas no jogo
    palavras_validas = filtrar_palavras(caracters=letras, limite=coletar_limite())
    print(f"Palavras válidas para o desafio ({len(palavras_validas)})=> ", palavras_validas)
    time.sleep(1)
    
    input_text = driver.find_element(By.ID, "input")
    
    index = 1
    
    # Coleta o runtime atual
    iniciar_timer = time.perf_counter()

    # Loop pelas palavras na lista de palavras válidas
    for palavra in palavras_validas:
        minimo = coletar_tamanho_minimo_das_palavras_faltantes(palavra)
        # Verifica se a palavra atual possui quantidade de caracteres maior ou igual ao tamanho mínimo
        if minimo:
            print(f"Testando palavra {index} de {len(palavras_validas)} => ", palavra)
            # Digita e envia a palavra
            try:
                input_text.send_keys(palavra)
                input_text.send_keys(Keys.ENTER)
                # Deleta a palavra atual para a entrada da próxima
                input_text.send_keys(Keys.CONTROL + 'a')
                input_text.send_keys(Keys.DELETE)
            except:
                print("Input não encontrado. Encerrando o jogo...")
                break
            time.sleep(0.2)
            
                
        # Caso a palavra atual seja menor que o tamanho mínimo, não será testada
        else:
            print(f"Pulando palavra {index} de {len(palavras_validas)} => ", palavra)
        index += 1
    time.sleep(3)
    
    # Caso não tenha encontrado todas as palavras, encerrará a partida
    try:
        botao_encerrar = driver.find_element(By.CSS_SELECTOR, 'button[title="Botão responsável por encerrar o jogo"]')
        botao_encerrar.click()
    except:
        pass
        
    # Coleta o runtime ao final da execução
    finalizar_timer = time.perf_counter()
    # Armazena o tempo de execução em minutos
    tempo_de_exec = round((finalizar_timer - iniciar_timer) / 60, 1)
    
    print("--------------------- Jogo finalizado! ----------------------")
    print("Tempo de execução (em minutos) =>", tempo_de_exec)
    qtd_acertos = driver.find_element(By.CSS_SELECTOR, ".points.svelte-9jj3fa").text
    print("Palavras encontradas => ", qtd_acertos)
    input("Pressione Enter para fechar o navegador...")
    driver.quit()
    
    