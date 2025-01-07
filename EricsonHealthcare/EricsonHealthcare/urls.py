from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import login_to_account

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('UserRole.urls')),
    path('case/', include('Case.urls')),
    path('visit/', include('Visit.urls')),
    path('question/', include('Question.urls')),
    path('report/', include('Reports.urls')),
    path('', include('FrontEnd.urls')),

    # Extra Admin urls
    path('custom-admin/login_to_account', login_to_account, name='login_to_account'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
