import os # Librería del sistema 
import subprocess as sp # Librería para ejecutar comandos en el sistema operativo


# Definimos las rutas de ejecución de los archivos que queremos abrir en windows
paths = {
    'notepad': "C:\\Windows\\System32\\notepad.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'cmd': "C:\\Windows\\System32\\cmd.exe",
    'opera gx': "C:\\Users\\Andres\\AppData\Local\\Programs\\Opera GX\\launcher.exe",
    'discord': "C:\\Users\\Andres\\AppData\\Local\\Discord\\app-1.0.9180\\Discord.exe"
}

# Definimos las funciones sin conexión

# Abrir camara
def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True) 

# Abrir Notepadd++
def open_notepad():
    os.startfile(paths['notepad'])

# Abrir discord
def open_discord():
    os.startfile(paths['discord'])

# Abrir consola de comandos
def open_cmd():
    os.system('start cmd')

# Abrir calculadora
def open_calculator():
    sp.Popen(paths['calculator'])

# Abrir opera
def open_chrome():
    os.startfile(paths['opera gx'])

