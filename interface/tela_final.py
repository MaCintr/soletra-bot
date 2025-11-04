from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def aviso_input_nao_encontrado():
    messagebox.showwarning("Campo não encontrado", "Falha ao encontrar campo de digitação. Jogo encerrado.")

def tela_final(tempo_de_exec, acertos):
    root = Tk()
    frm = ttk.Frame(root, padding=100)
    frm.grid()
    root.title("Soletra BOT - Fim de Jogo")
    # print("--------------------- Jogo finalizado! ----------------------")
    # print("Tempo de execução (em minutos) =>", tempo_de_exec)
    # qtd_acertos = driver.find_element(By.CSS_SELECTOR, ".points.svelte-9jj3fa").text
    # print("Palavras encontradas => ", qtd_acertos)
    # input("Pressione Enter para encerrar o programa...")
    ttk.Label(frm, text="Jogo finalizado!", font=("Arial", 16, "bold")).grid(column=0, row=0)
    ttk.Label(frm, text=(f"Tempo de execução (em minutos) => {tempo_de_exec}"), font=("Arial", 12)).grid(column=0, row=1)
    ttk.Label(frm, text=(f"Palavras descobertas => {acertos}"), font=("Arial", 12)).grid(column=0, row=2)
    ttk.Button(frm, text="Fechar", command=root.destroy).grid(column=0, row=3)
    root.mainloop()