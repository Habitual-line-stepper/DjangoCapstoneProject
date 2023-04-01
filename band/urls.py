"""
The URLs for the bands app.

This module defines the URL patterns for the bands app. The URL patterns include
views that are used to display home page, list of bands, login, registration,
profile, adding and editing a band.

Attributes:
    app_name (str): The name of the Django app.
    urlpatterns (list): The list of URL patterns for the bands app.
"""

from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from . import views
from .views import profile
from django.conf import settings
from django.conf.urls.static import static
from .views import BandListView

app_name = 'bands'

urlpatterns = [
    path("", views.home, name='home'),
    path('', BandListView.as_view(), name='band_list'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('bands/', views.band_list, name='band_list_noarg'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('add_band/', views.add_band, name='add_band'),
    path('edit_band/<int:pk>/', views.edit_band, name='edit_band'),
    path('accounts/profile/', profile, name='profile'),    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
