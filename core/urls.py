# Core imports.
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('chat/', include('apps.chat.urls')),
    path('admin/', admin.site.urls),
]
