import os 
import subprocess as sp

paths = {
    'notepad': "C:\\Windows\\System32\\notepad.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'cmd': "C:\\Windows\\System32\\cmd.exe",
    'chrome': "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
    'discord': "C:\\Users\\Andres\\AppData\\Local\\Discord\\app-1.0.9180\\Discord.exe"
}

# Abrir camara
def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

# Abrir Notepadd++ y Discord
def open_notepad():
    os.startfile(paths['notepad'])

def open_discord():
    os.startfile(paths['discord'])

# Abrir consola de comandos
def open_cmd():
    os.system('start cmd')

# Abrir calculadora
def open_calculator():
    sp.Popen(paths['calculator'])

    