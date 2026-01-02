import os
from PIL import Image

# Налаштування
BACKGROUND_PATH = "main_map.png"
AVATARS_DIR = "avatars/"
OUTPUT_PATH = "main_map.png"
AVATAR_SIZE = (100, 100) # Розмір маленької аватарки

def combine():
    # Відкриваємо фон
    bg = Image.open(BACKGROUND_PATH).convert("RGBA")
    
    # Отримуємо список усіх фото в папці avatars
    avatars = [f for f in os.listdir(AVATARS_DIR) if f.endswith(('.png', '.jpg', '.jpeg'))]
    
    x_offset = 50
    y_offset = 50

    for file in avatars:
        img = Image.open(os.path.join(AVATARS_DIR, file)).convert("RGBA")
        img = img.resize(AVATAR_SIZE)
        
        # Накладаємо аватарку на фон
        bg.paste(img, (x_offset, y_offset), img)
        
        # Зміщуємо координати для наступного фото (проста сітка)
        x_offset += 120
        if x_offset > bg.width - 100:
            x_offset = 50
            y_offset += 120

    # Зберігаємо результат
    bg.save(OUTPUT_PATH)
    print(f"Оновлено! Додано {len(avatars)} учасників.")

if __name__ == "__main__":
    combine()
