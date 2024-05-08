from django.contrib import admin
from django.urls import path
from .views import home, about, contact
urlpatterns = [
        path('', home),
        path('admin/', admin.site.urls),
        path('about/', about),
	    path('contact/', contact),
]