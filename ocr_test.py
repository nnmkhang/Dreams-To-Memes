from PIL import Image
from pytesseract import *

file = "C:\\Code\\Python\\Dreams-To-Memes\\test.jpg"



im = Image.open(file)
text = image_to_string(im, lang = "eng")
print(text)
