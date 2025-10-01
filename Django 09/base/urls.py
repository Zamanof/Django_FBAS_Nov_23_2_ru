from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),  # доступно по /todo/
    path('', include('todo.urls')),       # доступно по /
]


