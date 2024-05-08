import tkinter as tk
from tkinter import font, messagebox
import requests
import re
import openpyxl
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def Janela2():
    def is_valid_cnpj(cnpj):
        # Remove qualquer caracter que não seja número
        cnpj = re.sub(r'\D', '', cnpj)
        
        # Verifica se o CNPJ tem 14 dígitos
        if len(cnpj) != 14:
            return False
        
        # Verifica se todos os dígitos são iguais
        if len(set(cnpj)) == 1:
            return False
        
        # Calcula os dígitos verificadores
        soma = 0
        peso = 5
        for i in range(12):
            soma += int(cnpj[i]) * peso
            peso -= 1
            if peso < 2:
                peso = 9
        digito_1 = 0 if soma % 11 < 2 else 11 - soma % 11
        
        soma = 0
        peso = 6
        for i in range(13):
            soma += int(cnpj[i]) * peso
            peso -= 1
            if peso < 2:
                peso = 9
        digito_2 = 0 if soma % 11 < 2 else 11 - soma % 11
        
        # Verifica se os dígitos verificadores estão corretos
        return int(cnpj[12]) == digito_1 and int(cnpj[13]) == digito_2

    def getCNPJ(cnpj):
        if not is_valid_cnpj(cnpj):
            messagebox.showerror("Erro", "CNPJ inválido!")
            return
        
        loading_dialog = messagebox.showinfo("Aguarde", "Consultando CNPJ...")  # Exibe o pop-up de carregamento

        url = 'https://publica.cnpj.ws/cnpj/{}'.format(cnpj)
        r = requests.get(url)

        if r.status_code == 200:
            data = r.json()
            messagebox._show("Consulta", "Consulta Concluida!!!!")  # Fecha o pop-up de carregamento
            
            if 'erro' not in data:
                info_text.delete('1.0', tk.END)  # Limpa o conteúdo atual
                info_text.insert(tk.END, "Razão Social: ", 'bold')
                info_text.insert(tk.END, data['razao_social'] + "\n")
                
                info_text.insert(tk.END, "Nome Fantasia: ", 'bold')
                if data['estabelecimento']['nome_fantasia'] is not None:
                    info_text.insert(tk.END, data['estabelecimento']['nome_fantasia'] + "\n")
                else:
                    info_text.insert(tk.END, "Não possui nome fantasia\n", 'red')

                
                info_text.insert(tk.END, "Capital Inicial: ", 'bold')
                info_text.insert(tk.END, data['capital_social'] + "\n")
                
                info_text.insert(tk.END, "CNPJ: ", 'bold')
                info_text.insert(tk.END, data['estabelecimento']['cnpj'] + "\n")
                
                info_text.insert(tk.END, "Situação Cadastral: ", 'bold')
                info_text.insert(tk.END, data['estabelecimento']['situacao_cadastral'] + "\n")
                
                info_text.insert(tk.END, "Data Abertura: ", 'bold')
                info_text.insert(tk.END, data['estabelecimento']['data_inicio_atividade'] + "\n")
                
                info_text.insert(tk.END, "Endereço Completo:\n", 'bold')
                info_text.insert(tk.END, "Logradouro: ", 'bold')
                info_text.insert(tk.END, data['estabelecimento']['logradouro'] + "\n")
                
                info_text.insert(tk.END, "Número: ", 'bold')
                info_text.insert(tk.END, data['estabelecimento']['numero'] + "\n")
                
                info_text.insert(tk.END, "Complemento: ", 'bold')
                info_text.insert(tk.END, data['estabelecimento']['complemento'] + "\n")
                
                info_text.insert(tk.END, "Bairro: ", 'bold')
                info_text.insert(tk.END, data['estabelecimento']['bairro'] + "\n")
                
                info_text.insert(tk.END, "CEP: ", 'bold')
                info_text.insert(tk.END, data['estabelecimento']['cep'] + "\n")
                
                info_text.insert(tk.END, "Telefone 1: ", 'bold')
                info_text.insert(tk.END, f"({data['estabelecimento']['ddd1']}) {data['estabelecimento']['telefone1']}\n")
                
                info_text.insert(tk.END, "E-mail: ", 'bold')
                info_text.insert(tk.END, data['estabelecimento']['email'] + "\n")

                inscricoes_estaduais = data['estabelecimento'].get('inscricoes_estaduais', [])
                for inscricao in inscricoes_estaduais:
                    info_text.insert(tk.END, "\n""Inscrição Estadual: ", 'bold')
                    info_text.insert(tk.END, "{}\n".format(inscricao['inscricao_estadual']))
                    info_text.insert(tk.END, "Estado: ", 'bold')
                    info_text.insert(tk.END, "{}\n".format(inscricao['estado']['nome']))
                    info_text.insert(tk.END, "Ativo: ", 'bold')
                    if inscricao['ativo']:
                        info_text.insert(tk.END, "Ativo\n", 'green')
                    else:
                        info_text.insert(tk.END, "Não ativo\n", 'red')
                    info_text.insert(tk.END, "\n")


            else:
                messagebox.showerror("Erro", "CNPJ inválido!")
        else:
            messagebox.showerror("Erro", "Erro ao consultar o CNPJ!")

    def executar_codigo():
        cnpj = re.sub(r'\D', '', entrada.get())  # Remove pontuações do CNPJ
        getCNPJ(cnpj)

    def export_to_excel():
        # Crie um novo arquivo Excel
        wb = openpyxl.Workbook()
        ws = wb.active

        # Escreva as informações coletadas no Excel
        for index, line in enumerate(info_text.get("1.0", "end").splitlines()):
            ws.cell(row=index+1, column=1, value=line)

        # Salve o arquivo Excel
        wb.save("informacoes_cnpj.xlsx")
        messagebox.showinfo("Exportar para Excel", "As informações foram exportadas para um arquivo Excel com sucesso.")

    def export_to_pdf():
        # Crie um novo arquivo PDF
        c = canvas.Canvas("informacoes_cnpj.pdf", pagesize=letter)

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
    janela.title("CONSULTA CNPJ ##Desenvolvido por : Renan")

    # Crie um rótulo para instruções
    rotulo = tk.Label(janela, text="Digite o CNPJ que deseja consultar")
    rotulo.pack()

    # Crie uma entrada de texto
    entrada = tk.Entry(janela)
    entrada.pack()

    # Crie um botão para executar o código
    botao = tk.Button(janela, text="Consultar CNPJ", bg="blue", fg="white", command=executar_codigo)
    botao.pack()


    # Crie um widget Text para exibir as informações
    info_text = tk.Text(janela, wrap='word', height=20, width=80)
    info_text.pack()

    # Defina estilos de texto
    estilo = tk.font.Font(info_text, info_text.cget("font"))
    estilo.configure(weight='bold')
    info_text.tag_configure('bold', font=estilo)
    info_text.tag_configure('red', foreground='red')

    # Botão para exportar as informações para o Excel
    botao_exportar_excel = tk.Button(janela, text="Exportar para Excel", bg="blue", fg="white", command=export_to_excel)
    botao_exportar_excel.pack(side=tk.TOP, anchor=tk.CENTER, padx=5, pady=5)  # Define o lado superior e ancora no centro

    # Botão para exportar para PDF
    botao_exportar_pdf = tk.Button(janela, text="Exportar para PDF", bg="blue", fg="white", command=export_to_pdf)
    botao_exportar_pdf.pack(side=tk.TOP, anchor=tk.CENTER, padx=5, pady=5)  # Define o lado superior e ancora no centro



    # Inicie o loop de eventos da janela
    janela.mainloop()
