from io import BytesIO
import pytesseract
from PIL import Image
import requests

# Load the image using pytesseract
url = 'https://shop.cougarmtn.com/wp-content/uploads/2019/01/Sales-invoice-original.png'
response = requests.get(url)

imageOpened=Image.open(BytesIO(response.content))

ocr_result = pytesseract.image_to_string(imageOpened)

print(ocr_result)
