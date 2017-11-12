import numpy as np
import pytesseract
from PIL import Image


LANG = 'rus+eng'
TESSERACT_CONFIG = '--psm 7'


def recognize_text(image: np.ndarray) -> str:
    img = Image.fromarray(obj=image)
    text = pytesseract.image_to_string(image=img, lang=LANG, config=TESSERACT_CONFIG)
    return text
