from PIL import Image

img = Image.open("logo.jpg").convert("RGBA")
print("حجم الأصلي:", img.size)

# تأكد إنها مربعة (لو مش مربعة ضيف خلفية سودة)
w, h = img.size
size = max(w, h)
square = Image.new("RGBA", (size, size), (10, 14, 26, 255))

# حط الصورة في النص
offset = ((size - w) // 2, (size - h) // 2)
square.paste(img, offset, img if img.mode == "RGBA" else None)

# احفظ الأيقونات
square.resize((192, 192), Image.LANCZOS).save("icon-192.png", "PNG", optimize=True)
square.resize((512, 512), Image.LANCZOS).save("icon-512.png", "PNG", optimize=True)

print("✅ تم إنشاء:")
print("   - icon-192.png")
print("   - icon-512.png")
