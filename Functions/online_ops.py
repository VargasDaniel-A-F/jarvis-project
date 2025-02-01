import requests # Se utiliza para hacer peticiones HTTP a páginas web
import wikipedia # Permite buscar información en wikipedia desde python
import pywhatkit as kit # Ofrece varias funcionalidades como enviar mensajes  de whatsapp, buscar en youtube, etc.
from email.message import EmailMessage # forma  parte del modulo email de Python y permite crear correos  electronicos estructurados en formato MIME 
import smtplib # Se usa para enviar correos electronicos mediante el protocolo SMTP (Simple Mail Transfer Protocol)
from decouple import config # Permite gestionar variables de entorno y configuraciones sensibles sin exponerlas en el código fuente



# Encontrar mi dirección IP
def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json() # Hace una petición GET a la API de ipify para obtener la dirección IP pública del dispositivo
    return ip_address["ip"] # Devuelve la dirección IP pública del dispositivo

# Buscar en Wikipedia 
def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences = 2)
    return results

# Reproducir videos en youtube
def play_on_youtube(video):
    kit.playonyt(video) # Acepta un tema como elemento. Entonces busca dicho tema en youtube y reproduce el video más apropiado. Usa PyAutoGUI de manera encubierta.


# Buscar en Google
def search_on_google(query):
    kit.search(query)


# Enviar un mensaje vía WhatsApp (Hay que asegurarse de tener la sesión de WhatsApp web activada)
def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+57{number}", message) 


# Enviar un email. Para hacer esto, debemos tener el módulo "smtplib" preinstalado.
EMAIL = config("EMAIL") # Importamos el correo electrónico desde el archivo .env
PASSWORD = config("PASSWORD") # Importamos la contraseña desde el archivo .env

def send_email(receiver_address, subject, message): # 3 parametros: dirección de correo electrónico del destinatario, asunto y mensaje
    try:
        email = EmailMessage() # Crea un objeto EmailMessage
        email['To'] = receiver_address # Establecemos la dirección de correo electrónico del destinatario
        email["Subject"] = subject # Establecemos el asunto del correo electrónico
        email["From"] = EMAIL # Establecemos la dirección de correo electrónico del remitente
        email.set_content(message) # Establecemos el mensaje del correo electrónico
        s = smtplib.SMTP("smtp.gmail.com", 587) # Creamos un objeto de clase SMTP del módulo smtplib. Toma un host y un port number como parametros
        s.startttls() # Inicia el protocolo de seguridad TLS
        s.login(EMAIL, PASSWORD) # Inicia sesión en la cuenta de correo electrónico
        s.send_message(email) # Envía el correo electrónico
        s.close() # Cierra la conexión SMTP
        return True
    except Exception as e:
        print(e)
        return False
    

# Obtener los últimos titulares de las noticias

NEWS_API_KEY = config("NEWS_API_KEY") # Importamos la API key de newsapi.org desde el archivo .env

def get_latest_news():
    news_headlines = [] # Creamos una lista vacía para almacenar los titulares de las noticias
    res = requests.get(f"https://newsapi.org/v2/top-headlines?country=co&apiKey={NEWS_API_KEY}&category=general").json() # Hace una petición GET a la API de newsapi.org para obtener los titulares de las noticias
    articles = res["articles"] # Obtiene los artículos de la respuesta JSON
    for article in articles: # Itera sobre los artículos
        news_headlines.append(article["title"]) # Agrega el titular del artículo a la lista de titulares de las noticias
    return news_headlines[:5] # Devuelve los primeros 5 titulares de las noticias


# Obtener reporte del clima 
OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID") # Importamos la API key de openweathermap.org desde el archivo .env

def get_weather_report(city):
    res = requests.get(f"htpps://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json() # Hace una petición GET a la API de openweathermap.org para obtener el clima de la ciudad
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}°C", f"{feels_like}°C"


# Obtener peliculas en tendencia

TMDB_API_KEY = config("TMDB_API_KEY") # Importamos la API key de themoviedb.org desde el archivo .env

def get_trending_movies():
    trending_movies = [] # Creamos una lista vacía para almacenar las películas en tendencia
    res = requests.get(f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json() # Hace una petición GET a la API de themoviedb.org para obtener las películas en tendencia
    results = res["results"] # Obtiene los resultados de la respuesta JSON
    for r in results: # Itera sobre los resultados
        trending_movies.append(r["original_title"])
    return trending_movies[:5] # Devuelve las primeras 5 películas en tendencia


# FUNCION PARA HACER CHISTE ALEATORIAMENTE

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json() # Hace una petición GET a la API de icanhazdadjoke.com para obtener un chiste aleatorio
    return res["joke"]


# Obtener un consejo al azar
def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json() # Hace una petición GET a la API de adviceslip.com para obtener un consejo aleatorio
    return res['slip']['advice']

