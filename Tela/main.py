import tkinter as tk
from consulta_cep import Janela1
from consulta_cnpj import Janela2

# Crie a janela principal
janela_principal = tk.Tk()
janela_principal.title("Janela Principal")

# Função para abrir a janela de consulta de CEP
def abrir_janela_cep():
    Janela1()

# Função para abrir a janela de consulta de CNPJ
def abrir_janela_cnpj():
    Janela2()

# Botão para abrir a janela de consulta de CEP
botao_janela1 = tk.Button(janela_principal, text="Consulta CEP", command=abrir_janela_cep)
botao_janela1.pack()

# Botão para consultar CNPJ
botao_janela2 = tk.Button(janela_principal, text="Consultar CNPJ", command=abrir_janela_cnpj)
botao_janela2.pack()

# Inicie o loop de eventos da janela principal
janela_principal.mainloop()
