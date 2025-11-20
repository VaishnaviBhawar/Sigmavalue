from django.contrib import admin
from django.urls import path   # 👈 ADD THIS
from django.http import HttpResponse

from api.views import get_locations, analyze_location

def home(request):
    return HttpResponse("Backend is running successfully!")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('data/', get_locations),
    path('analyze/', analyze_location),
]
