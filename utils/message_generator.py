from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_message(name, goal, activity, tone, length):
    prompt = f"""
    Create a {length.lower()} motivational message for someone named {name}.
    Their wellness goal is '{goal}', and they prefer '{activity}' as activities.
    Use a {tone.lower()} tone.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a motivational wellness coach."},
            {"role": "user", "content": prompt.strip()}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()
