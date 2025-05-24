from fastapi import FastAPI, Request, HTTPException # Importa HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
import logging # Para logging

app = FastAPI()

# Configuración básica de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Habilita CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OLLAMA_MODEL = "llama3"
OLLAMA_URL = "http://ollama:11434/api/chat"

class Mensaje(BaseModel):
    message: str

@app.post("/api/chat")
async def chat(mensaje: Mensaje):
    logger.info(f"Received message from backend: {mensaje.message}")

    messages = [
        {"role": "system", "content": "Eres un asistente útil."},
        {"role": "user", "content": mensaje.message}
    ]

    try:
        ollama_request_payload = {
            "model": OLLAMA_MODEL,
            "messages": messages,
            "stream": False
        }
        
        logger.info(f"Sending request to Ollama: {ollama_request_payload}")

        response = requests.post(OLLAMA_URL, json=ollama_request_payload, timeout=300) # Añadir timeout

        logger.info(f"Received status from Ollama: {response.status_code}")
        logger.info(f"Received response from Ollama: {response.text}") # Log completo de la respuesta

        if response.status_code == 200:
            ollama_data = response.json()
            
            # **MODIFICACIÓN CLAVE AQUÍ:**
            # Asegúrate de que la estructura JSON es la esperada
            if "message" in ollama_data and "content" in ollama_data["message"]:
                respuesta = ollama_data["message"]["content"]
                logger.info(f"Ollama response content: {respuesta}")
                return {"response": respuesta}
            else:
                logger.error(f"Ollama response missing 'message' or 'content' key: {ollama_data}")
                # Podrías querer devolver un error más específico aquí
                raise HTTPException(status_code=500, detail="Estructura de respuesta de Ollama inesperada.")
        else:
            logger.error(f"Ollama returned an error status: {response.status_code} - {response.text}")
            raise HTTPException(status_code=response.status_code, detail=f"Ollama no respondió correctamente: {response.text}")
            
    except requests.exceptions.RequestException as req_e:
        logger.error(f"Network or request error connecting to Ollama: {req_e}")
        raise HTTPException(status_code=503, detail=f"Error de red al conectar con Ollama: {req_e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred in chatbot-api: {e}", exc_info=True) # exc_info para stack trace completo
        raise HTTPException(status_code=500, detail=f"Error interno en chatbot-api: {e}")