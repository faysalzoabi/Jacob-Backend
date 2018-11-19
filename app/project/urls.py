from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

mypatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='Jacob Rest API')),
]

urlpatterns = [
    path('backend/', include(mypatterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)