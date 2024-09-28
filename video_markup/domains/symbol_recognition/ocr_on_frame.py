import pytesseract
from PIL import Image

def ocr_on_frame(frame):
    text = pytesseract.image_to_string(Image.fromarray(frame), lang='rus')
    return text