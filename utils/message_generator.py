import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_message(name, goal, activity, tone, length):
    prompt = f"""Generate a {length}-line motivational message for {name} who is focused on {goal}.
    They prefer doing {activity} and like a {tone} motivational tone. Keep it energetic and actionable."""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
