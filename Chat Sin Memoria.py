import os
import warnings
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import time

warnings.filterwarnings("ignore")

# 🔐 Cargar variables desde el archivo .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ No se encontró OPENAI_API_KEY en el archivo .env")

# 🤖 Configuración del modelo OpenRouter
llm = ChatOpenAI(
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=os.environ["OPENAI_API_KEY"],
    model_name="cohere/north-mini-code:free",
    temperature=1
)

print("💬 Chatbot vía OpenRouter (escribe 'salir' para terminar)\n")

Meta_prompt = """
"""

while True:
    user_input = input("👤 Tú: ")

    if user_input.lower() in ["salir", "exit", "quit"]:
        print("👋 Hasta luego.")
        break

    try:
        # Se envía únicamente el metaprompt y el mensaje actual del usuario
        response = llm.invoke([
            HumanMessage(
                content=f"Condiciones: {Meta_prompt}\nUsuario: {user_input}"
            )
        ])

        # Mostrar respuesta
        if hasattr(response, "content"):
            print(f"🤖 Bot: {response.content.strip()}\n")

        elif isinstance(response, dict) and "content" in response:
            print(f"🤖 Bot: {response['content'].strip()}\n")

        elif isinstance(response, list) and len(response) > 0:
            print(f"🤖 Bot: {response[0].content.strip()}\n")

        else:
            print(f"🤖 Bot: {response}\n")

        time.sleep(2)

    except Exception as e:
        print(f"❌ Error: {e}\n")