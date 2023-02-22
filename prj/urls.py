from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from cms.views import CustomerHTMxTableView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CustomerHTMxTableView.as_view(), name='customer_htmx')
]

if settings.LOGIN_OPEN:
    urlpatterns += [
        path('accounts/', include('accounts.urls')),
    ]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)), 
    ]    

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)