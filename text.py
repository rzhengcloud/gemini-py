
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv() # This loads variables from .env into os.environ

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))



#    You don't need a separate 'client' object.
model = genai.GenerativeModel("gemini-2.0-flash") # Use the model name here

response = model.generate_content(
    contents="Explain how AI works in a few words. Say hello to the user. say caonima",
)

print(response.text)