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
engine.setProperty('voice', voices[0].id) # Establecemos la voz del engine. La primera (0) corresponde a una voz femenina, la segunda (1) corresponde a una voz masculina.


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


# Importamos las funciones de los archivos de funciones
import requests
from Functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message
from Functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_discord
from pprint import pprint


if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'open notepad' in query:
            open_notepad()

        elif 'open discord' in query:
            open_discord()

        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()

        elif 'open camera' in query:
            open_camera()

        elif 'open calculator' in query:
            open_calculator()

        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f"Su dirección IP es {ip_address}.\n Para su comodidad la estoy mostrando en la pantalla, señor.")
            print(f"Su dirección IP es {ip_address}")

        elif 'wikipedia' in query:
            speak('¿Qué quiere buscar en wikipedia, señor?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"De acuerdo con Wikipedia, {results}")
            speak("Para su comodidad, la estoy mostrando en la pantalla, señor.")
            print(results)

        elif 'youtube' in query:
            speak('¿Qué quieres ver en YouTube, señor?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            speak('¿Qué quiere buscar en Google, señor?')
            query = take_user_input().lower()
            search_on_google(query)

        elif "send whatsapp message" in query:
            speak('A quien le quieres enviar el mensaje, señor?')
            number = take_user_input().lower()
            speak("¿Qué mensaje le quieres enviar?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("El mensaje ha sido enviado, señor.")

        elif "send an email" in query:
            speak("A quien le quiere enviar el correo, señor?")
            receiver_address = input("Escriba el correo electrónico del destinatario: ")
            speak("¿Cual es el asunto?")
            subject = take_user_input().capitalize()
            speak("¿Cual es el mensaje")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("El correo ha sido enviado, señor.")
            else:
                speak("Algo ha salido mal mientras estaba enviando el correo, por favor revise el registro de errores")

        elif 'joke' in query:
            speak(f"Espero le guste este, señor")
            joke = get_random_joke()
            speak(joke)
            speak("Para su comodidad, la estoy mostrando en la pantalla, señor.")
            pprint(joke)

        elif "advice" in query:
            speak(f"Aqui está, señor")
            advice = get_random_advice()
            speak(advice)
            speak("Para su comodidad, la estoy mostrando en la pantalla, señor.")
            pprint(advice)

        elif "trending movies" in query:
            speak(f"Algunas de las peliculas en tendencia son: {get_trending_movies()}")
            speak("Para su mejor comprensión, las estoy mostrando en la pantalla, señor.")
            print(*get_trending_movies(), sep = '\n')


        elif "news" in query:
            speak(f"Estoy leyendo los ultimos titulares de las noticias")
            speak(get_latest_news())
            speak("Para su comodidad, las mostraré en pantalla, señor")
            print(*get_latest_news(), sep = '\n')	

        elif "weather" in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Obteniendo el reporte del clima en su ciudad {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"La temperatura actual es {temperature} grados centigrados, pero se siente más como {feels_like} grados centigrados")
            speak(f"Además, el reporte menciona acerca de {weather}")
            speak("Para vuestra información, se la mostraré en pantalla, señor")
            print(f"Reporte del clima de {city}:\n {weather}\nTemperatura actual: {temperature}°C\nSensación térmica: {feels_like}°C")

        elif "turn off" in query:
            break
            
