import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GuestsBlog.settings')
django.setup()

from blog.models import Post

TOPICS = [
    "Майбутнє Frontend-розробки", "Чому FSD — це круто", "Як вивчити Django за ніч",
    "Pixel Perfect: міф чи реальність?", "Топ 10 бібліотек для React", 
    "Секрети продуктивності Junior-розробника", "Мій досвід у SoftServe",
    "Пригоди в світі Python ORM", "Найкращі аніме для програмістів",
    "Цифровий детокс: як вижити без коду", "Zustand проти Redux",
    "Next.js 15: що нового?", "Як налаштувати Tailwind правильно"
]

LOREM = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
    "Sed do eiusmod tempor incididunt ut labore et et dolore magna aliqua. ",
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. ",
    "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. ",
    "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia. ",
    "Curabitur pretium tincidunt lacus. Nulla gravida orci a odio. ",
    "Nullam varius, turpis et commodo pharetra, est eros bibendum elit. "
]

def generate_content(min_sentences=3, max_sentences=10):
    count = random.randint(min_sentences, max_sentences)
    return "".join(random.choices(LOREM, k=count))

def seed_data():
    print("Очищення старої бази...")
    Post.objects.all().delete()
    
    print("Генерація 50 різноманітних постів...")
    for i in range(1, 51):
        topic = random.choice(TOPICS)
        content = generate_content(5, 15)
        
        Post.objects.create(
            title=f"{topic} #{i}",
            content=content,
            author_name=f"Developer_{random.randint(1, 10)}"
        )
        
        if i % 10 == 0:
            print(f"Створено {i} постів...")

    print("\nГотово! База даних заповнена. Тепер можеш перевіряти 5-колонну сітку та пагінацію.")

if __name__ == '__main__':
    seed_data()