
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static 
from django.conf import settings
from django.views.static import serve
from django.urls import re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('brands/', include('brands.urls')),
    path('product/', include('product.urls')),
    path('blogs', include('blog.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    

handler404 = 'home.views.custom_404'