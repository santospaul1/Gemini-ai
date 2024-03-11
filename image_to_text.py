from PIL import Image
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

GOOGLE_API_KEY="AIzaSyDcCiSIyOlrjMO1rqGEvH2n4Mk_ARr8g00"
genai.configure(api_key=GOOGLE_API_KEY)
'''
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
'''
#text from image only

img = Image.open('image.jpg')

model = genai.GenerativeModel('gemini-pro-vision')
response = model.generate_content(img)
to_markdown(response.text)

response = model.generate_content(["Write a story from the image", img])
to_markdown(response.text)
print(response.text)



