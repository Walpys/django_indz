from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def get_post_list(request):
    return HttpResponse("<h1>Список постів</h1><p>Тут буде перелік усіх записів.</p>")

def get_post_detail(request, post_id):
    return HttpResponse(f"<h1>Перегляд поста №{post_id}</h1><p>Зміст окремого поста.</p>")

def post_create(request):
    return HttpResponse("<h1>Створення нового поста</h1><form>Форма буде тут.</form>")

def add_comment(request, post_id):
    return HttpResponse(f"<h1>Додавання коментаря</h1><p>Ви коментуєте пост №{post_id}.</p>")