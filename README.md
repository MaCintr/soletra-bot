# Soletra Bot

Um bot automatizado desenvolvido em Python + Selenium que joga o jogo Soletra do G1 (https://g1.globo.com/jogos/soletra/), identificando automaticamente as letras do desafio e tentando acertar todas as palavras com base em um dicionário externo.

## 🚀 Funcionalidades

🧠 Leitura automática das letras disponíveis no jogo (incluindo a letra obrigatória).

📚 Filtro inteligente de palavras baseado em um dicionário em português.

⚡ Preenchimento e envio automatizado das palavras válidas no campo de entrada do jogo.

🔍 Modo tentativa e erro otimizado para maximizar o número de acertos.

## ⚙️ Requisitos

Python 3.10+

Microsoft Edge instalado

## ⚙️ Dependências:

selenium 
webdriver-manager

## 🧠 Como Funciona

1. O bot abre o jogo Soletra usando o Selenium.

2. Lê todas as letras disponíveis na tela (letra central (obrigatória) e externas).

3. Usa o módulo solver/word_filter.py para filtrar palavras válidas do dicionário:
  - Entre 4 caracteres até o limite do jogo atual
  - Contendo apenas letras do desafio
  - Incluindo obrigatoriamente a letra central

4. Digita automaticamente as palavras encontradas e pressiona ENTER.

## ▶️ Como Executar

Clone o repositório:

```git clone https://github.com/seuusuario/soletra-bot.git```
```cd soletra-bot```

Instale as dependências:

```pip install -r requirements.txt```

Execute o bot:

```python main.py```

## 📚 Dicionário Utilizado

O projeto utiliza um dicionário de palavras em português disponível em:
🔗 [AlfredoFilho/Palavras_PT-BR](https://github.com/AlfredoFilho/Palavras_PT-BR/blob/master/Palavras_PT-BR.txt)

## 🧩 Exemplo de Saída
```---------------- Iniciando jogo ----------------```

```------------- Fechando instruções --------------```

```Letras encontradas =>  ['A', 'B', 'R', 'O', 'T', 'E', 'M']```

```Palavras válidas para o desafio (102) =>  ['AMOR', 'ATEMO', 'BERA', 'ROMA', ...]```

```Testando palavra 1 de 102 =>  AMOR```

```Testando palavra 2 de 102 =>  ATEMO```

```...```

```Lista de palavras percorrida com sucesso!```

```-------------- Encerrando partida --------------```
