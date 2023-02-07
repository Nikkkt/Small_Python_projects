import PySimpleGUI as sg

layout = [
    [sg.Input(key = 'INPUT'), sg.Spin(['km to mile   ', 'm to km      ', 'cm to m      ', 'sec to min   ', 'sec to hours ', 'grams to kg  ', 'grams to tons'], key = 'UNITS'), 
    sg.Button('Convert', key = 'BUTTON')],
    [sg.Text('Output', key = 'OUTPUT')]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'BUTTON':
        input_value = values['INPUT']
        if input_value.isnumeric():
            match values['UNITS']:

                case 'km to mile     ':
                    output = round(float(input_value) * 0.6214, 2)
                    output_string = f'{input_value} km are {output} miles'

                case 'm to km      ':
                    output = float(input_value) * 0.001
                    output_string = f'{input_value} m are {output} km'

                case 'cm to m      ':
                    output = float(input_value) * 0.01
                    output_string = f'{input_value} cm are {output} m'

                case 'sec to min   ':
                    output = round(float(input_value) / 60, 2)
                    output_string = f'{input_value} seconds are {output} minutes'

                case 'sec to hours ':
                    output = round(float(input_value) / 3600, 4)
                    output_string = f'{input_value} seconds are {output} hours'

                case 'grams to kg   ':
                    output = round(float(input_value) / 10**3, 3)
                    output_string = f'{input_value} grams are {output} kg'

                case 'grams to tons':
                    output = round(float(input_value) / 10**6, 6)
                    output_string = f'{input_value} grams are {output} tons'

            window['OUTPUT'].update(output_string)

        else:
            window['OUTPUT'].update('ERROR. ENTER A NUMBER')

window.close()