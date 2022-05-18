import os
from PIL import Image, ImageFilter, ImageDraw, ImageFont

for i in os.listdir('.'):
    if i.endswith('.jpg'):
        img = Image.open(i)
        fn, flext = os.path.splitext(i)

        rs = img.convert('L')
        rs1 = rs.filter(ImageFilter.DETAIL)
        rs2 = rs1.resize((1080, 1080))
        width, height = rs2.size

        draw = ImageDraw.Draw(rs2)
        text = "#X_X_X!"
        title = "HELLO"
        font = ImageFont.truetype("georgia.ttf", 85)
        textwidth, textheight = draw.textsize(text, font)

        space = 15
        x = width - textwidth - space
        y = height - textheight - space

        draw.text((x, y), text, title, font=font)
        rs2.save('qqq/{}{}'.format(fn, flext))