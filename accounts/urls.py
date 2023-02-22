from django.urls import path, include
from django.conf import settings

from .views import CustomLoginView

urlpatterns = [
    path(
        'login/',
        CustomLoginView.as_view(template_name="registration/login.html"),
        name="auth_login",
    ),                      
]

if settings.LOGIN_OPEN:
    urlpatterns += [
        path('', include('registration.backends.default.urls')), 
    ]