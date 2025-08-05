import os
import openai

def responder_pergunta(pergunta_usuario):
    pergunta_usuario = pergunta_usuario.lower()

    base = ""
    for arquivo in ["contexto_faq.txt", "contexto_ppt.txt", "contexto_pdf.txt"]:
        try:
            with open(f"app/{arquivo}", "r", encoding="utf-8") as f:
                base += f.read() + "\n"
        except:
            pass

    prompt = f"""
Você é um atendente da Flora Energia. Responda à pergunta de forma objetiva, simples e no estilo humano da Flora. Use como base os materiais oficiais abaixo. 
Se não souber a resposta, diga: 'Essa dúvida será encaminhada para um humano da equipe Flora. 🌱'

Materiais de apoio:
"""
{base}
"""

Pergunta: {pergunta_usuario}
Resposta:
"""

    try:
        resposta = openai.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
        )
        return resposta.choices[0].message.content.strip()
    except Exception:
        return "Essa dúvida será encaminhada para um humano da equipe Flora. 🌱"