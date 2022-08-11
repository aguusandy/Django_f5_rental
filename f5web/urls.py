
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

handler404 = 'alquiler.views.error_404_view'

urlpatterns = [
    url(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$',serve,{'document_root':settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', include('alquiler.urls')),
    path('members/', include('django.contrib.auth.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

