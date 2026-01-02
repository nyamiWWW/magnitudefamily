import os
import random
from PIL import Image

def process():
    bg = Image.open("main_map.png").convert("RGBA")
    width, height = bg.size
    
    avatar_files = os.listdir("avatars/")
    
    for file in avatar_files:
        if file.endswith(('.png', '.jpg')):
            img = Image.open(f"avatars/{file}").convert("RGBA")
            img = img.resize((100, 100)) # Розмір зірки
            
            # Випадкові координати
            x = random.randint(0, width - 100)
            y = random.randint(0, height - 100)
            
            bg.paste(img, (x, y), img)
    
    bg.save("main_map.png")
    # Додаємо лічильник
    print(f"Карту оновлено. Учасників: {len(avatar_files)}")

process()
