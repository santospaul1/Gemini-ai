import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

#from google.colab import userdata

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

GOOGLE_API_KEY="Your_API_Key"
genai.configure(api_key=GOOGLE_API_KEY)
'''
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
'''
#text only
model = genai.GenerativeModel('gemini-pro')


response = model.generate_content("What are the courses of poverty in Africa", stream=True)
#print text directly without stream
#to_markdown(response.text)
#print(response.text)

#To stream text
for chunk in response:
  print(chunk.text)
  print("_"*80)


  
