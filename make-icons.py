from PIL import Image, ImageDraw, ImageFont
import os

def make_icon(size, filename):
    img = Image.new('RGB', (size, size), '#0F1724')
    draw = ImageDraw.Draw(img)
    # دايرة ذهبية
    margin = size // 8
    draw.ellipse([margin, margin, size-margin, size-margin], 
                 fill='#E3A84B', outline='#172234', width=size//32)
    # حرف R
    try:
        font = ImageFont.truetype("/system/fonts/Roboto-Bold.ttf", size//2)
    except:
        font = ImageFont.load_default()
    text = "R"
    bbox = draw.textbbox((0,0), text, font=font)
    w, h = bbox[2]-bbox[0], bbox[3]-bbox[1]
    draw.text(((size-w)/2, (size-h)/2 - size//16), text, fill='#1A1305', font=font)
    img.save(filename)
    print(f"✅ {filename}")

make_icon(192, "icon-192.png")
make_icon(512, "icon-512.png")
