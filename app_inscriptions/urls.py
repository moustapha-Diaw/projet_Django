from django.contrib import admin
from django.urls import path, include

app_name = 'dashboard'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("inscription.urls")),
   
]


