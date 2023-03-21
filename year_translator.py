import PySimpleGUI as sg

a = sg.Spin(values=('民國', '西元'),initial_value='民國')

layout = [[sg.Text('請輸入年份')],
          [a, sg.Input(key='INPUT')],
          [sg.Text(key='OUTPUT')],
          [sg.Button('start'),sg.Button('quit')]
          ]

window = sg.Window('年份轉換', layout)

while True:
    event, values = window.read()
    input_num = values['INPUT']

    if event == sg.WINDOW_CLOSED or event == 'quit':
        break
    if input_num.isnumeric():
        if a.get() == '民國':
            result = f'西元{round(float(input_num)) + 1911}年'
            window['OUTPUT'].update(result)
        else:
            result = f'民國{round(float(input_num)) - 1911}年'
            window['OUTPUT'].update(result)
    else:
        window['OUTPUT'].update('請重新輸入數字!!')