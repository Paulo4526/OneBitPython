import tkinter as tk
from encodings.utf_7 import encode

# 1 - Criando a janela no windows
window = tk.Tk()
window.geometry("300x150")
window.title("Gerenciador de Frases")

# 2 - Adicionando o frame da janela
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill="x", expand=True)

# 3 - Adicionando Label
label = tk.Label(frame, text="Hello World")
label.pack(fill="x", expand=True)

# 4 - Adicionando o input
#Label do input
frase_lab = tk.Label(frame, text="Frase")
frase_lab.pack(fill="x", expand=True)
#Input
frase_inp = tk.Entry(frame)
frase_inp.pack(fill="x", expand=True)

# 5 - Função que altera o label
def click():
    label.config(text=frase_inp.get())

# 6 - Adicionando o Button do input
button = tk.Button(frame, text="Enviar", command=click)
button.pack()

window.mainloop()