from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def aviso_input_nao_encontrado():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    messagebox.showerror("Campo não encontrado", "Falha ao encontrar campo de digitação. Jogo encerrado.", parent=root)
    root.destroy()


def tela_final(tempo_de_exec, acertos):
    root = Tk()
    root.attributes('-topmost', True)
    frm = ttk.Frame(root, padding=100)
    frm.grid()
    root.title("Soletra BOT - Fim de Jogo")
    ttk.Label(frm, text="Jogo finalizado!", font=("Arial", 16, "bold")).grid(column=0, row=0)
    ttk.Label(frm, text=(f"Tempo de execução (em minutos) => {tempo_de_exec}"), font=("Arial", 12)).grid(column=0, row=1)
    ttk.Label(frm, text=(f"Palavras descobertas => {acertos}"), font=("Arial", 12)).grid(column=0, row=2)
    ttk.Button(frm, text="Fechar", command=root.destroy).grid(column=0, row=3)
    root.mainloop()