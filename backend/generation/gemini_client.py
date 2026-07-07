from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_response(prompt):

    interaction = client.interactions.create(
        model="gemini-2.5-flash",
        input=prompt
    )
    return interaction.output_text
