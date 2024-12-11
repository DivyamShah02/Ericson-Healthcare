from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('UserRole.urls')),
    path('case/', include('Case.urls')),
    path('visit/', include('Visit.urls')),
    path('', include('FrontEnd.urls')),
]
