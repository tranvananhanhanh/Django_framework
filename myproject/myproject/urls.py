
from django.contrib import admin
from django.urls import path,include
from myapp import views


urlpatterns = [
    path('', views.home, name='home'), 
    path('about/' ,views.about,name='about'),
    path('menu/' ,views.menu,name='menu'),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('book/',views.book_table,name='book'),

    path('admin/', admin.site.urls),  # Đảm bảo rằng đường dẫn admin đã được thêm
    path('tags/',views.tags),
    path('login/',views.login),




]
