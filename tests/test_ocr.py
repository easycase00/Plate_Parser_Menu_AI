from PIL import Image
from menu.ocr import extract_text_from_image

def test_extract_text_from_image():
    sample_image = Image.new("RGB", (200, 100), color=(255, 255, 255))
    result = extract_text_from_image(sample_image)
    assert isinstance(result, str)
