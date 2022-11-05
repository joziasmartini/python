# A registration screen using the PySimpleGUI lib

import PySimpleGUI as sg

# Define the window's contents
layout = [
    [sg.Text("Username"), sg.InputText()],
    [sg.Text("Password"), sg.InputText(password_char="*")],
    [sg.Button("Ok"), sg.Button("Cancel")]
]

# Create the window
window = sg.Window("Registration Screen", layout)

# Display and interact with the Window
event, values = window.read()

# Do something with the information gathered
print("Username:", values[0])
print("Password:", values[1])

# Finish up by removing from the screen
window.close()