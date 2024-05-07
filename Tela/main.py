from tkinter import font, messagebox, ttk
import tkinter as tk
#from consulta_cep import consulta_cep1
from consulta_cnpj import Janela1



# Crie a janela principal
janela_principal = tk.Tk()
janela_principal.title("Janela Principal")

# # Crie botões para abrir outras janelas
# botao_janela1 = tk.Button(janela_principal, text="Abrir Janela 1", command=consulta_cep1)
# botao_janela1.pack()

botao_janela2 = tk.Button(janela_principal, text="Consultar CNPJ", command=Janela1)
botao_janela2.pack()

# Inicie o loop de eventos da janela principal
janela_principal.mainloop()
Janela1()