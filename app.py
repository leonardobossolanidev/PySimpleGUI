import PySimpleGUI as sg
import csv
import os

# Função para salvar os dados no CSV
def salvar_usuario(nome, email, idade):
    with open("usuarios.csv", "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, email, idade])

# Função para ler os dados do CSV
def carregar_usuarios():
    if not os.path.exists("usuarios.csv"):
        return []
    with open("usuarios.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        return list(leitor)

# Layout da interface
layout = [
    [sg.Text("Nome:"), sg.InputText(key="nome")],
    [sg.Text("Email:"), sg.InputText(key="email")],
    [sg.Text("Idade:"), sg.InputText(key="idade")],
    [sg.Button("Salvar"), sg.Button("Mostrar Usuários"), sg.Button("Sair")],
    [sg.Text("Usuários Cadastrados:")],
    [sg.Multiline(size=(50, 10), key="output", disabled=True)]
]

# Criar a janela
janela = sg.Window("Cadastro de Usuários", layout)

# Loop de eventos
while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED or evento == "Sair":
        break
    elif evento == "Salvar":
        nome = valores["nome"]
        email = valores["email"]
        idade = valores["idade"]

        if nome and email and idade.isdigit():
            salvar_usuario(nome, email, idade)
            sg.popup("Usuário salvo com sucesso!")
            janela["nome"].update("")
            janela["email"].update("")
            janela["idade"].update("")
        else:
            sg.popup_error("Preencha todos os campos corretamente!")
    elif evento == "Mostrar Usuários":
        usuarios = carregar_usuarios()
        texto = "\n".join([f"{u[0]} | {u[1]} | {u[2]} anos" for u in usuarios])
        janela["output"].update(texto)

# Encerrar o programa
janela.close()
