import tkinter as tk
from tkinter import font, messagebox
import requests
import re
import openpyxl
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def Janela1():
    def validate_cep(cep):
        if len(cep) != 8 or not cep.isdigit():
            messagebox.showerror("Erro", "CEP inválido! O CEP deve conter exatamente 8 dígitos.")
            return
        
        loading_dialog = messagebox.showinfo("Aguarde", "Consultando CEP...")  # Exibe o pop-up de carregamento

        url = 'https://viacep.com.br/ws/{}/json/'.format(cep)
        r = requests.get(url)

        if r.status_code == 200:
            data = r.json()
            messagebox._show("Consulta", "Consulta Concluída!!!!")  # Fecha o pop-up de carregamento
            
            if 'erro' not in data:
                info_text.delete('1.0', tk.END)  # Limpa o conteúdo atual
                
                info_text.insert(tk.END, "CEP: ", 'bold')
                info_text.insert(tk.END, data['cep'] + "\n")
                
                info_text.insert(tk.END, "Logradouro: ", 'bold')
                info_text.insert(tk.END, data['logradouro'] + "\n")
                
                info_text.insert(tk.END, "Complemento: ", 'bold')
                info_text.insert(tk.END, data['complemento'] + "\n")
                
                info_text.insert(tk.END, "Bairro: ", 'bold')
                info_text.insert(tk.END, data['bairro'] + "\n")
                
                info_text.insert(tk.END, "Localidade: ", 'bold')
                info_text.insert(tk.END, data['localidade'] + "\n")
                
                info_text.insert(tk.END, "UF: ", 'bold')
                info_text.insert(tk.END, data['uf'] + "\n")
                
                info_text.insert(tk.END, "IBGE: ", 'bold')
                info_text.insert(tk.END, data['ibge'] + "\n")
                
                info_text.insert(tk.END, "GIA: ", 'bold')
                info_text.insert(tk.END, data['gia'] + "\n")
                
                info_text.insert(tk.END, "DDD: ", 'bold')
                info_text.insert(tk.END, data['ddd'] + "\n")
                
                info_text.insert(tk.END, "SIAFI: ", 'bold')
                info_text.insert(tk.END, data['siafi'] + "\n")
                
            else:
                messagebox.showerror("Erro", "CEP inválido!")
        else:
            messagebox.showerror("Erro", "Erro ao consultar o CEP!")

    def executar_codigo():
        cep = re.sub(r'\D', '', entrada.get())  # Remove pontuações do CEP
        validate_cep(cep)

    def export_to_excel():
        # Crie um novo arquivo Excel
        wb = openpyxl.Workbook()
        ws = wb.active

        # Escreva as informações coletadas no Excel
        for index, line in enumerate(info_text.get("1.0", "end").splitlines()):
            ws.cell(row=index+1, column=1, value=line)

        # Salve o arquivo Excel
        wb.save("informacoes_cep.xlsx")
        messagebox.showinfo("Exportar para Excel", "As informações foram exportadas para um arquivo Excel com sucesso.")

    def export_to_pdf():
        # Crie um novo arquivo PDF
        c = canvas.Canvas("informacoes_cep.pdf", pagesize=letter)

        # Adicione as informações coletadas ao PDF
        y = 750  # Posição inicial vertical
        for line in info_text.get("1.0", "end").splitlines():
            c.drawString(100, y, line)
            y -= 12  # Ajuste para a próxima linha

        # Salve o PDF
        c.save()
        messagebox.showinfo("Exportar para PDF", "As informações foram exportadas para um arquivo PDF com sucesso.")

    # Crie a janela principal
    janela = tk.Tk()
    janela.title("CONSULTA CEP ##Desenvolvido por : Renan")

    # Crie um rótulo para instruções
    rotulo = tk.Label(janela, text="Digite o CEP que deseja consultar")
    rotulo.pack()

    # Crie uma entrada de texto
    entrada = tk.Entry(janela)
    entrada.pack()

    # Crie um botão para executar o código
    botao = tk.Button(janela, text="Consultar CEP", bg="blue", fg="white", command=executar_codigo)
    botao.pack()

    # Crie um widget Text para exibir as informações
    info_text = tk.Text(janela, wrap='word', height=20, width=80)
    info_text.pack()

    # Defina estilos de texto
    estilo = tk.font.Font(info_text, info_text.cget("font"))
    estilo.configure(weight='bold')
    info_text.tag_configure('bold', font=estilo)

    # Botão para exportar as informações para o Excel
    botao_exportar_excel = tk.Button(janela, text="Exportar para Excel", bg="blue", fg="white", command=export_to_excel)
    botao_exportar_excel.pack(side=tk.TOP, anchor=tk.CENTER, padx=5, pady=5)  # Define o lado superior e ancora no centro

    # Botão para exportar para PDF
    botao_exportar_pdf = tk.Button(janela, text="Exportar para PDF", bg="blue", fg="white", command=export_to_pdf)
    botao_exportar_pdf.pack(side=tk.TOP, anchor=tk.CENTER, padx=5, pady=5)  # Define o lado superior e ancora no centro

    # Inicie o loop de eventos da janela
    janela.mainloop()
