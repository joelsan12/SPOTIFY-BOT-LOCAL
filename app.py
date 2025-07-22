import spotipy
from spotipy.oauth2 import SpotifyOAuth
import speech_recognition as sr
import time

# Configura tus credenciales
CLIENT_ID = ''
CLIENT_SECRET = ''
REDIRECT_URI = ''
SCOPE = 'user-modify-playback-state user-read-playback-state user-read-currently-playing'

# Inicializa autenticación OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
    open_browser=False  # si no quieres que abra el navegador otra vez
))

# Reconocimiento por voz
def escuchar_comando():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Di el nombre de la canción que quieres reproducir:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        texto = recognizer.recognize_google(audio, language='es-ES')
        print(f"🎧 Has dicho: {texto}")
        return texto
    except sr.UnknownValueError:
        print("❌ No se entendió el comando.")
    except sr.RequestError as e:
        print(f"❌ Error con el reconocimiento de voz: {e}")
    return None

# Buscar canción en Spotify
def buscar_cancion(nombre):
    resultado = sp.search(q=nombre, type='track', limit=1)
    tracks = resultado['tracks']['items']
    if not tracks:
        print("❌ No se encontró la canción.")
        return None
    track = tracks[0]
    print(f"✅ Encontrado: {track['name']} - {track['artists'][0]['name']}")
    return track['uri']

# Obtener dispositivo activo
def obtener_dispositivo():
    devices = sp.devices()
    if not devices['devices']:
        print("❌ No hay dispositivos activos. Abre la app de Spotify en tu PC.")
        return None
    return devices['devices'][0]['id']

# Reproducir la canción
def reproducir(uri):
    device_id = obtener_dispositivo()
    if device_id:
        sp.start_playback(device_id=device_id, uris=[uri])
        print("▶️ Reproduciendo canción...")
    else:
        print("❌ No se pudo reproducir.")

# Programa principal
def main():
    while True:
        comando = escuchar_comando()
        if comando:
            if "salir" in comando.lower():
                print("👋 Cerrando bot.")
                break
            uri = buscar_cancion(comando)
            if uri:
                reproducir(uri)
        time.sleep(1)

if __name__ == "__main__":
    main()
