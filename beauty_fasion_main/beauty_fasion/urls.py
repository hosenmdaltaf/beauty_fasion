
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('service/', include('servicepage.urls')),
    path('contact/', include('contactpage.urls')),
    path('blog/', include('blogpage.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
   
]

if settings.DEBUG:
    #urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
