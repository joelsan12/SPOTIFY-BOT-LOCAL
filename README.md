🟥 GRATIS <br>
🟥 INTEGRACION DE MAS COMANDOS: PAUSA, CONTINUAR, SKIP, SIGUIENTE....
🟥 INTERFAZ
🟥 MODE DE VOICE ASSISTANT O ACCESIBILITY SERVICE APP

<h1>
  DATO: SOLO FUNCIONA CON UNA CUENTA SUSCRITA DE SPOTIFY
</h1>


# 🎵 Control de Spotify por Voz con Python

Este proyecto permite controlar Spotify con comandos de voz usando **Spotipy** y **SpeechRecognition**.  
Puedes buscar y reproducir canciones con solo hablar.

## 🚀 Requisitos
- Python 3.8 o superior
- Cuenta de [Spotify Developer](https://developer.spotify.com)
- Tener un dispositivo Spotify abierto (PC, teléfono, o web player)


<img width="800" height="750" alt="image" src="https://github.com/user-attachments/assets/117a3ec1-64eb-48d2-b4a5-ca659cb18b7f" />


<p>
  Uso de Cliente Id, Client Secrert del Dashboard de desarrollador para crear enlace con el bot y el Spotify.
</p> </br>

<h2> USO DE DATOS DEL DASHBOARD DE DESARROLLADOR EN CODIGO</h2>

1. Clona el repositorio:
   ```bash
   git clone https://github.com/joelsan12/SPOTIFY-BOT-LOCAL.git
   cd SPOTIFY-BOT-LOCAL
Crea un entorno virtual (opcional pero recomendado):

2. Opcional... Crea y activa un entorno virtual

python -m venv venv
venv\Scripts\activate

3. Instala las dependencias:
  ```bash
  pip install spotipy SpeechRecognition pyaudio
```

4. Agrega tus credenciales de Spotify:
Puedes hacerlo directamente en `app.py` o utilizar un archivo `.env`:
  
   CLIENT_ID=tu_client_id
   CLIENT_SECRET=tu_client_secret
   REDIRECT_URI=http://localhost:8080/callback

5. Ejecuta el bot:
 ```bash
 python app.py
```

### 2. **Uso / Instrucciones**

- Abre Spotify en tu dispositivo.
- Ejecuta el script con `python app.py`.
- Di el nombre de la canción que deseas reproducir.
- Para salir, di “salir” o presiona `Ctrl+C`.

### 3. **Explicación general del código**

Agregar un breve resumen de las funciones:
- `escuchar_comando()`: escucha tu voz y convierte el audio en texto.
- `buscar_cancion(nombre)`: busca la canción más relevante en Spotify.
- `obtener_dispositivo()`: identifica el dispositivo activo.
- `reproducir(uri)`: inicia la reproducción de la canción.

