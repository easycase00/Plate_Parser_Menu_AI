import easyocr
import numpy as np
from PIL import Image

reader = easyocr.Reader(['en'])

def extract_text_from_image(image: Image.Image) -> str:
    image_np = np.array(image)
    result = reader.readtext(image_np, detail=0)
    return "\n".join(result)
