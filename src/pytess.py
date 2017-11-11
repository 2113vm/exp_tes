from typing import List

import numpy as np
import pytesseract
from PIL import Image


LANG = None
TESSERACT_CONFIG = None


def recognize_text(image: np.ndarray) -> str:
    img = Image.fromarray(obj=image)
    text = pytesseract.image_to_string(image=img, lang=LANG, config=TESSERACT_CONFIG)
    return text
