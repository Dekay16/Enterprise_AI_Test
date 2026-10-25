import os
from openai import OpenAI

client = OpenAI()

MODEL = os.getenv("OPENAI_MODEL", "gpt-5.5")


def ask_ai(question: str) -> str:
    response = client.responses.create(
        model=MODEL,
        instructions=(
            "You are an internal IT support assistant. "
            "Be clear, concise, and honest when you don't know something."
        ),
        input=question,
    )

    return response.output_text


if __name__ == "__main__":
    question = input("Ask a question: ")
    answer = ask_ai(question)
    print("\nAI response:")
    print(answer)