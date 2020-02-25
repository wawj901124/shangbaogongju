import pytesseract
from PIL import Image

image = Image.open('timg.jpg')
code = pytesseract.image_to_string(image)
print(code)