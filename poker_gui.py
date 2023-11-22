import PySimpleGUI as sg
import poker_functional as pf

suits = ['C','H','D','S']
ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

rs0 = sg.Spin(ranks,key = '-RS0-')
rs1 = sg.Spin(ranks,key = '-RS1-')
rs2 = sg.Spin(ranks,key = '-RS2-')
rs3 = sg.Spin(ranks,key = '-RS3-')
rs4 = sg.Spin(ranks,key = '-RS4-')
rs5 = sg.Spin(ranks,key = '-RS5-')
rs6 = sg.Spin(ranks,key = '-RS6-')
rs7 = sg.Spin(ranks,key = '-RS7-')
rs8 = sg.Spin(ranks,key = '-RS8-')
rs9 = sg.Spin(ranks,key = '-RS9-')

ss0 = sg.Spin(suits,key = '-SS0-')
ss1 = sg.Spin(suits,key = '-SS1-')
ss2 = sg.Spin(suits,key = '-SS2-')
ss3 = sg.Spin(suits,key = '-SS3-')
ss4 = sg.Spin(suits,key = '-SS4-')
ss5 = sg.Spin(suits,key = '-SS5-')
ss6 = sg.Spin(suits,key = '-SS6-')
ss7 = sg.Spin(suits,key = '-SS7-')
ss8 = sg.Spin(suits,key = '-SS8-')
ss9 = sg.Spin(suits,key = '-SS9-')



col1 = [
    [sg.Text("Hand 1")],
    [rs0,ss0],
    [rs1,ss1],
    [rs2,ss2],
    [rs3,ss3],
    [rs4,ss4]
]

col2 = [
    [sg.Text("Hand 2")],
    [rs5,ss5],
    [rs6,ss6],
    [rs7,ss7],
    [rs8,ss8],
    [rs9,ss9]
]

col3 =[
    [sg.Button("Compare",key = "-COMPARE-")],
    [sg.Text("Hand 1 Value : "),sg.Text(key="-HAND1VALUE-")],
    [sg.Text("Hand 2 Value : "),sg.Text(key="-HAND2VALUE-")],
    [sg.Text(key="-RESULT-")]
]
layout = [
    [sg.Column(col1),
    sg.Column(col2),
    sg.Column(col3)],
]

layout2 = [
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
        hand1 = [values["-RS0-"]+values["-SS0-"],
                values["-RS1-"]+values["-SS1-"],
                values["-RS2-"]+values["-SS2-"],
                values["-RS3-"]+values["-SS3-"],
                values["-RS4-"]+values["-SS4-"]]
        
        hand1set = set(hand1)
        if len(hand1set) != 5:
            sg.popup("Hand 1 has to have unique cards")
            continue
        
        hand2 = [values["-RS5-"]+values["-SS5-"],
                values["-RS6-"]+values["-SS6-"],
                values["-RS7-"]+values["-SS7-"],
                values["-RS8-"]+values["-SS8-"],
                values["-RS9-"]+values["-SS9-"]]

        hand2set = set(hand2)
        if len(hand2set ) != 5:
            sg.popup("Hand 2 has to have unique cards")
            continue

        if not hand1set.isdisjoint(hand2set):
            sg.popup("Hands cannot share the same cards")
            continue

        hand1_bin = pf.strlist2binarylist(hand1)
        
        hand2_bin = pf.strlist2binarylist(hand2)
        
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