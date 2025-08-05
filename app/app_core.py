
import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("fontes/base_faq.json", encoding="utf-8") as f:
    base_faq = json.load(f)

def responder_pergunta(pergunta):
    pergunta = pergunta.strip().lower()
    for item in base_faq:
        if item["pergunta"].lower() in pergunta:
            return item["resposta"]

    resposta = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.5,
        messages=[
            {"role": "system", "content": "Você é um atendente da Flora Energia. Responda de forma objetiva, simples e com base na identidade da Flora. Use os documentos fornecidos e o site www.floraenergia.com.br como fonte. Caso não saiba a resposta, indique que um humano da equipe irá ajudar."},
            {"role": "user", "content": pergunta}
        ]
    )
    return resposta.choices[0].message.content
