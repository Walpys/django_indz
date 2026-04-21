
from django.contrib import admin
from django.urls import path
from blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_post_list, name='post_list'),
    path('post/<int:post_id>/', views.get_post_detail, name='post_detail'),
    path('new/', views.post_create, name='post_create'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
]