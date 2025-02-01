import pyttsx3 # Librería multiplataforma de texto a voz que es independiente a la plataforma donde se ejecute. Trabaja sin conexión.
from decouple import config 

USERNAME = config('USER') # Importación del nombre de usuario desde el archivo .env
BOTNAME = config('BOTNAME') # Importación del nombre del bot desde el archivo .env

engine = pyttsx3.init('sapi5') # Inicializamos un engine 


# Set rate
engine.setProperty('rate', 190) 

# Set volume
engine.setProperty('volume', 1.0)

# Set voice (Male)
voices = engine.getProperty('voices') # Inicializamos una variable que contiene las voces disponibles
engine.setProperty('voice', voices[0].id) # Establecemos la voz del engine. La primera (0) corresponde a una voz masculina, la segunda (1) corresponde a una voz femenina.


# Conversión texto a voz
# La función speak() será la responsable de enunciar cualquier texto que pase por ella
def speak(text): 
    """Usado para decir cualquier texto que le sea entregado"""
    engine.say(text) # El engine va a decir el texto que le entreguemos
    engine.runAndWait() # Se bloquea durante el bucle de eventos y vuelve cuando se borra la cola de comandos


# Función dar la bienvenida
# Esta función será usada para dar la bienvenida al usuario cada momento que el programa se ejcuta. En concordancia con el horario en tiempo real, saludará.
from datetime import datetime # Importamos el módulo datetime

def greet_user():
    """Saluda al usuario de acuerdo al horario"""

    hour = datetime.now().hour

    if (hour >= 6) and (hour < 12):
        speak(f"Buenos días {USERNAME}")
    elif (hour >= 12) and (hour < 18):
        speak(f"Buenas tardes {USERNAME}")
    elif (hour >= 18) and (hour < 22):
        speak(f"Buenas noches {USERNAME}")
    speak(f"Yo soy {BOTNAME} ¿Cómo puedo asistirle?")
    

# Obtener información del usuario
# Usamos esta función para poder tomar instrucciones o comandos por parte del usuario y también poder reconocer el comando usando el módulo speech_recognition

import speech_recognition as sr # Importamos el módulo speech_recognition
from random import choice # Importamos el módulo choice
from utils import opening_text # Importamos la lista de frases de bienvenida desde el archivo utils.py

def take_user_input():
    """Toma las entradas del usuario, las reconoce utilizando el módulo de reconocimiento de voz y lo transforma a texto"""

    r = sr.Recognizer() # Inicializamos un objeto de reconocimiento de voz con la clase Recognizer
    with sr.Microphone() as source: # Con el microfono como source
        print('Escuchando...') 
        r.pause_threshold = 1 # No compila, aunque hagamos una pausa de 1 segundo mientras hablamos
        audio = r.listen(source) # Escuchamos el audio

    try: # Tratamos de reconocer el audio
        print('Reconociendo...')
        query = r.recognize_google(audio, language = 'es-es') # Utilizamos el reconocimiento de voz usando la API de reconocimiento de voz de Google. El lenguaje es español de España. Se guarda una cadena de texto en "query"
        if not 'Salir' in query or 'Alto' in query: # Si la variable query no tiene las palabras "salir" o "alto" en ella
            speak(choice(opening_text)) # Nos confirma la orden
        else: # Si la variable query tiene las palabras "salir" o "alto" en ella
            hour = datetime.now().hour # Lee la hora actual
            if hour >= 22 and hour < 6: # Si la hora actual es mayor o igual a 22 y menor a 6
                speak('Buenas noches señor ¡Cuidese!') # Se despide
            else: # De otra manera, se despide
                speak('Tenga buen día señor')

            exit() # Sale del programa
    except Exception: # Si no se puede reconocer el audio
        speak('Disculpe, no he podido entender ¿Podría decirlo de nuevo?') # Se le pide que lo diga de nuevo
        query = 'None' # Se guarda la cadena de texto "None" en la variable query
    return query # Al finalizar, se devuelve la variable query

print("")



