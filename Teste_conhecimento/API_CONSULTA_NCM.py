import tkinter as tk
from tkinter import font, messagebox
import requests
import re
import openpyxl
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def formatar_data(data):
    data_obj = datetime.strptime(data, '%Y-%m-%d')
    data_formatada = data_obj.strftime('%d/%m/%Y')
    return data_formatada

def obter_data_atual():
    return datetime.now().date()

def insert_text_with_color(text, color):
    info_text.insert(tk.END, text, color)

def validate_ncm(ncm):
    if len(ncm) != 8 or not ncm.isdigit():
        messagebox.showerror("Erro", "NCM inválido! O NCM deve conter exatamente 8 dígitos.")
        return False
    return True

info_consultada = False

def getncm(ncm):
    global info_consultada
    if not validate_ncm(ncm):
        return

    loading_dialog = messagebox.showinfo("Aguarde", "Consultando NCM...")
    url = 'https://brasilapi.com.br/api/ncm/v1/{}'.format(ncm)
    r = requests.get(url)
    messagebox.showinfo("Consulta", "Consulta Concluída!!!!")

    if r.status_code == 200:
        data = r.json()
        if 'erro' not in data:
            info_text.delete('1.0', tk.END)

            info_text.insert(tk.END, "Código: ", 'bold')
            info_text.insert(tk.END, data['codigo'] + "\n")

            info_text.insert(tk.END, "Descrição: ", 'bold')
            info_text.insert(tk.END, data['descricao'] + "\n")

            info_text.insert(tk.END, "Data Inicio: ", 'bold')
            info_text.insert(tk.END, formatar_data(data['data_inicio']) + "\n")

            data_atual = obter_data_atual()
            data_fim_formatada = formatar_data(data['data_fim'])
            
            data_fim = datetime.strptime(data['data_fim'], '%Y-%m-%d').date()
            if data_fim < data_atual:
                insert_text_with_color("Data de Expiração: ", 'bold')
                insert_text_with_color(data_fim_formatada + " (NCM EXPIRADO)\n", 'red')
            else:
                info_text.insert(tk.END, "Data de Expiração: ", 'bold')
                info_text.insert(tk.END, data_fim_formatada + "\n")
            
            # Define que as informações foram consultadas com sucesso
            info_consultada = True
        else:
            messagebox.showerror("Erro", "NCM inválido ou Vencido!")
    else:
        messagebox.showerror("Erro", "NCM inválido ou Vencido!")

def export_to_excel():
    global info_consultada
    if info_consultada == True:
        ncm = re.sub(r'\D', '', entrada.get())
        wb = openpyxl.Workbook()
        ws = wb.active
        for index, line in enumerate(info_text.get("1.0", "end").splitlines()):
            ws.cell(row=index+1, column=1, value=line)
        wb.save(f"informacoes_ncm_{ncm}.xlsx")
        messagebox.showinfo("Exportar para Excel", "As informações foram exportadas para um arquivo Excel com sucesso.")
    else:
        messagebox.showwarning("Aviso", "Nenhuma informação foi consultada. Não é possível exportar para o Excel.")

def export_to_pdf():
    global info_consultada
    if info_consultada == True:
        ncm = re.sub(r'\D', '', entrada.get())
        c = canvas.Canvas(f"informacoes_ncm_{ncm}.pdf", pagesize=letter)
        y = 750
        for line in info_text.get("1.0", "end").splitlines():
            c.drawString(100, y, line)
            y -= 12
        c.save()
        messagebox.showinfo("Exportar para PDF", "As informações foram exportadas para um arquivo PDF com sucesso.")
    else:
        messagebox.showwarning("Aviso", "Nenhuma informação foi consultada. Não é possível exportar para o PDF.")
        


def executar_codigo():
    global info_consultada
    ncm = re.sub(r'\D', '', entrada.get())
    getncm(ncm)
    botao_exportar_excel.config(state=tk.NORMAL) 
    botao_exportar_pdf.config(state=tk.NORMAL)



        

# Crie a janela principal
janela = tk.Tk()
janela.title("CONSULTA NCM ##Desenvolvido por : Renan")

# Crie um rótulo para instruções
rotulo = tk.Label(janela, text="Digite o NCM que deseja consultar")
rotulo.pack()

# Crie uma entrada de texto
entrada = tk.Entry(janela)
entrada.pack()

# Crie um botão para executar o código
botao = tk.Button(janela, text="Consultar NCM", bg="blue", fg="white", command=executar_codigo)
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
botao_exportar_excel.pack(side=tk.TOP, anchor=tk.CENTER, padx=5, pady=5)
botao_exportar_excel.config(state=tk.DISABLED)  # Inicialmente, desativa o botão

# Botão para exportar para PDF
botao_exportar_pdf = tk.Button(janela, text="Exportar para PDF", bg="blue", fg="white", command=export_to_pdf)
botao_exportar_pdf.pack(side=tk.TOP, anchor=tk.CENTER, padx=5, pady=5)
botao_exportar_pdf.config(state=tk.DISABLED)  # Inicialmente, desativa o botão

# Inicie o loop de eventos da janela
janela.mainloop()
