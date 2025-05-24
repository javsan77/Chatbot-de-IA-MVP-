# 🤖 Chatbot de IA (MVP)

Este proyecto implementa un chatbot conversacional impulsado por un Large Language Model (LLM). Construido con una arquitectura de microservicios contenerizada con Docker Compose, el sistema busca ser modular, escalable y eficiente.

## ✨ Características Actuales

* **Asistente Conversacional:** Capaz de comprender el lenguaje natural y generar respuestas coherentes utilizando el modelo Llama 3.
* **Arquitectura de Microservicios:** Desacoplamiento de servicios (Frontend, Backend, API de Chatbot, Servidor LLM) para facilitar el desarrollo y escalabilidad.
* **Contenerización con Docker Compose:** Todos los componentes se ejecutan en contenedores Docker, simplificando el despliegue y asegurando la portabilidad.
* **Frontend Simplificado:** Una interfaz de usuario web básica en HTML/CSS/JavaScript que permite la interacción con el chatbot.
* **Proxy Inverso Nginx:** Gestiona el tráfico del frontend y lo redirige al backend API.
* **Logging Integrado:** Captura información de logs en cada servicio para facilitar la depuración y monitoreo.

## 🚀 Arquitectura del Proyecto (MVP)

El proyecto sigue una arquitectura de microservicios para la modularidad y escalabilidad.

_Diagrama de la arquitectura del chatbot, mostrando los componentes y el flujo de comunicación._

1.  **`frontend` (Nginx + HTML/CSS/JS):**
    * **Nginx:** Sirve los archivos estáticos de la interfaz de usuario y actúa como proxy inverso para enrutar las solicitudes API al `backend`.
    * **HTML/CSS/JS:** Proporciona una interfaz de chat básica y funcional para la interacción del usuario.
2.  **`backend` (Spring Boot - Java):**
    * Actúa como la capa de orquestación intermedia.
    * Recibe las solicitudes del `frontend` (vía Nginx) y las reenvía al `chatbot-api`.
    * Punto ideal para implementar lógica de negocio adicional, autenticación y futuras integraciones.
3.  **`chatbot-api` (FastAPI - Python):**
    * El servicio principal para la interacción con el LLM.
    * Recibe la pregunta del usuario del `backend`.
    * Gestiona la comunicación con el servidor Ollama.
    * Actualmente utiliza un prompt de sistema básico y se conecta de forma síncrona a Ollama.
4.  **`ollama` (Servidor LLM Local):**
    * Contenedor Docker que aloja y sirve el modelo de lenguaje grande (LLM), `Llama 3`.
    * Permite ejecutar el LLM localmente sin depender de APIs externas, ofreciendo mayor control.

## 🛠️ Tecnologías Utilizadas

* **Frontend:** Nginx, HTML, CSS, JavaScript (puro)
* **Backend:** Java (Spring Boot), Maven
* **API del Chatbot:** Python (FastAPI), `requests`, `pydantic`, `logging`
* **Modelo de Lenguaje:** Llama 3 (servido vía Ollama)
* **Contenerización:** Docker, Docker Compose

## ⚙️ Cómo Ejecutar el Proyecto

Asegúrate de tener Docker y Docker Compose instalados en tu sistema.

1.  **Clona el Repositorio:**

2.  **Iniciar Ollama y Descargar el Modelo:**
    * Primero, levanta solo el servicio de Ollama para asegurarte de que esté listo para descargar el modelo.
    ```bash
    docker compose build ollama
    docker compose up -d
    docker exec -it ollama ollama run llama3
    
3.  **Verificar que todo funcione:**
        ◦ Ollama: http://localhost:11434 
        ◦ API Python: http://localhost:8000 
        ◦ Backend Java: http://localhost:8080 
        ◦ Frontend: http://localhost:3000 

    
    
    
    
