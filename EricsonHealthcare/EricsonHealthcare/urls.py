from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import login_to_account, add_city
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url='/static/logo.png')),
    path('user/', include('UserRole.urls')),
    path('case/', include('Case.urls')),
    path('visit/', include('Visit.urls')),
    path('question/', include('Question.urls')),
    path('report/', include('Reports.urls')),
    path('', include('FrontEnd.urls')),

    # Extra Admin urls
    path('custom-admin/login_to_account', login_to_account, name='login_to_account'),
    path('custom-admin-add-visit', add_city, name='add_city'),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
