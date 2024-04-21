import PySimpleGUI as sg

sg.theme('reddit')

layout = [
    [sg.Text('E-mail'),sg.Input(key='email')],
    [sg.Text('Senha'),sg.Input(key='senha', password_char='*')],
    [sg.FolderBrowse('Escolher pasta Anexo', target='input_axexos'),sg.Input(key='input_anexo')],
    [sg.FolderBrowse('Escolher pasta Planilha', target='input_planilhas'),sg.Input(key='input_planilhas')],
    [sg.Button('Salvar')]
]

janela = sg.Window('Principal', layout=layout)

while True:
    event, value = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Salvar':
        email = value['email']
        senha = value['senha']
        caminho_pasta_axexo = value['input_anexo']
        caminho_pasta_planilha = value['input_planilha']
        print(f'O email degitado foi {email}')
        print(f'a senha digitada foi {senha}')
        print(f'o caminho da pasta anexo é {caminho_pasta_axexo}')
        print(f'o caminho da planilha é {email}')