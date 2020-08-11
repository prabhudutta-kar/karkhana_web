import requests
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

x = requests.get('./quiz.htmlpython')
print(x.status_code)


data = pd.read_excel (r'') 
name_list = data["Name"].tolist() 
for i in name_list:
    im = Image.open(r'')
    d = ImageDraw.Draw(im)
    location = (100, 398)
    text_color = (0, 137, 209)
    font = ImageFont.truetype("arial.ttf", 120)
    d.text(location, i, fill = text_color, font = font)
    im.save("certificate_" + i + ".pdf")
