
from dotenv import load_dotenv
import os
import google.generativeai as genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64

load_dotenv() # This loads variables from .env into os.environ

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))



#    You don't need a separate 'client' object.
model = genai.GenerativeModel("gemini-2.0-flash-preview-image-generation") # Use the model name here
contents = ('Hi, can you create a 3d rendered image of a pig '
            'with wings and a top hat flying over a happy '
            'futuristic scifi city with lots of greenery?')

# response = model.generate_content(
#     contents=contents,
#     generation_config=types.GenerateContentConfig(
#       response_modalities=['TEXT', 'IMAGE']
#     )
# )
response = model.generate_content(
    contents=contents,
    generation_config={
        "response_modalities": ['TEXT', 'IMAGE']
    }
)



for part in response.candidates[0].content.parts:
  if part.text is not None:
    print(part.text)
    print("* * *")
  elif part.inline_data is not None:
    image = Image.open(BytesIO((part.inline_data.data)))
    image.save('gemini-native-image.png')
    image.show()