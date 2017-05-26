import pytesseract
from PIL import Image
from PIL import ImageEnhance
img_name = 'captcha1.png'
im = Image.open(img_name)
enhancer = ImageEnhance.Color(im)
enhancer = enhancer.enhance(0)
enhancer = ImageEnhance.Brightness(enhancer)
enhancer = enhancer.enhance(2)
enhancer = ImageEnhance.Contrast(enhancer)
enhancer = enhancer.enhance(8)
enhancer = ImageEnhance.Sharpness(enhancer)
im = enhancer.enhance(20)
im.show()
capttxt = pytesseract.image_to_string(im)
x = capttxt.split()
capttxt = ''.join(x)
print(capttxt)
