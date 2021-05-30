import PySimpleGUI as sg
from index import main, apenasNumeros

# Tema
sg.theme('DarkAmber')

# Layout
layout = [
    [sg.Text("Calculadora IMC")],
    [sg.Text('Peso:'),sg.InputText(key='peso')],
    [sg.Text('Altura'),sg.InputText(key='altura')],
    [sg.Button('Comfirmar'), sg.Cancel(),],
    [sg.Text(key='-OUTPUT-',size=(45,1))]
]
# Criando a janela
window = sg.Window('Calculadora IMC', layout)

while True:
    # Ler os eventos e valores.
    event, values = window.read()

    # Finalizar 
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif event == 'Comfirmar':
        peso = values['peso'];
        altura = values['altura'];

        peso = apenasNumeros(peso)
        altura = apenasNumeros(altura)

        window['-OUTPUT-'].update(main(peso,altura))
        

window.close()