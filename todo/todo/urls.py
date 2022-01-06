from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('todo_maker.urls',namespace='todo_maker')),
    path('admin/', admin.site.urls),
]   