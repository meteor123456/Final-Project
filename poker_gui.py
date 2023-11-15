import PySimpleGUI as sg
import poker_functional as pf

layout = [
    [sg.Text("Hand 1: "), sg.Input(key="-HAND1-"), sg.Text("Value: "),sg.Text(key="-HAND1VALUE-")],
    [sg.Text("Hand 2: "), sg.Input(key="-HAND2-"), sg.Text("Value: "),sg.Text(key="-HAND2VALUE-")],
    [sg.Button("Compare",key = "-COMPARE-"),sg.Text(key="-RESULT-")]
]

window = sg.Window('Poker Hand Evalulator', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "-COMPARE-":
        hand1_bin = pf.str2binarylist(values["-HAND1-"])
        hand2_bin = pf.str2binarylist(values["-HAND2-"])
        val1 = pf.evaluatehand(hand1_bin);
        val2 = pf.evaluatehand(hand2_bin);
        window["-HAND1VALUE-"].update(str(bin(val1)) + " = " + str(val1));
        window["-HAND2VALUE-"].update(str(bin(val2)) + " = " + str(val2));
        if val1 > val2:
            window["-RESULT-"].update("Hand 1 wins!")
        elif val1 < val2:
            window["-RESULT-"].update("Hand 2 wins!")
        else:
            window["-RESULT-"].update("Tie")

window.close()