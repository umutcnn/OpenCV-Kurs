from PIL import Image
import pytesseract

im = Image.open("test.png")
text = pytesseract.image_to_string(im,lang="tur")
print(text)