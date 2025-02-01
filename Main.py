import pyttsx3
from decouple import config

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

engine = pyttsx3.init('sapi5')


# Set rate
engine.setProperty('rate', 190)

# Set volume
engine.setProperty('volume', 1.0)

# Set voice (Male)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Conversión texto a voz
def speak(text):
    """Usado para decir cualquier texto que le sea entregado"""
    engine.say(text)
    engine.runAndWait()


# Función dar la bienvenida

from datetime import datetime

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
import speech_recognition as sr
from random import choice 
from utils import opening_text

def take_user_input():
    """Toma las entradas del usuario, las reconoce utilizando el módulo de reconocimiento de voz y lo transforma a texto"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Escuchando...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Reconociendo...')
        query = r.recognize_google(audio, language = 'es-es')
        if not 'Salir' in query or 'Alto' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 22 and hour < 6:
                speak('Buenas noches señor ¡Cuidese!')
            else:
                speak('Tenga buen día señor')

            exit()
    except Exception:
        speak('Disculpe, no he podido entender ¿Podría decirlo de nuevo?')
        query = 'None'
    return query 

print("")


        