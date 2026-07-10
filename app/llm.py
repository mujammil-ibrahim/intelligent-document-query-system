from openai import OpenAI
from app.config import OPENROUTER_API_KEY, MODEL_NAME

print("OPENROUTER_API_KEY:", OPENROUTER_API_KEY)

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)

def ask_llm(question: str, context: str):

    prompt = f"""
You are an AI assistant.

Answer ONLY using the provided context.

If the answer is not present, reply:
"I couldn't find that information in the uploaded document."

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content