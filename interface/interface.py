from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from time import sleep
from scraper.game_reader import resolver_soletra

root = Tk()
root.attributes('-topmost', True)


def iniciar_jogo():
    root.destroy()
    messagebox.showinfo("Instruções", "Após clicar em OK, o robô irá abrir o site do Soletra\n e iniciar o jogo. Evite usar o mouse para não interferir na execução.")
    resolver_soletra()

def renderizar_programa():
    frm = ttk.Frame(root, padding=100)
    frm.grid()
    root.title("Soletra BOT")
    ttk.Label(frm, text="Soletra BOT", font=("Arial", 20, "bold")).grid(column=0, row=0)
    ttk.Label(frm, justify="center", text="Um bot automatizado desenvolvido em Python + Selenium\nque joga o jogo Soletra do G1 (https://g1.globo.com/jogos/soletra/),\n identificando automaticamente as letras do desafio e tentando\n acertar todas as palavras com base em um dicionário de palavras\n do Português Brasileiro.").grid(column=0, row=1)
    # ttk.Label(frm, text="Instruções:", font=("Arial", 10, "bold")).grid(column=0, row=2)
    # ttk.Label(frm, justify="center", text="Após clicar no botão Iniciar, o robô irá abrir o site do Soletra\n e iniciar o jogo. Evite usar o mouse para não interferir na execução.").grid(column=0, row=3)
    ttk.Button(frm, text="Iniciar", command=iniciar_jogo).grid(column=0, row=3)
    ttk.Button(frm, text="Fechar", command=root.destroy).grid(column=0, row=4)

    # ttk.Button(frm, text="Fechar", command=root.destroy).grid(column=1, row=4)
    root.mainloop()
    
