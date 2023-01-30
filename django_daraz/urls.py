from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views import defaults
from guardian import views
from django.views.static import serve

defaults.page_not_found = views.not_found_view
handler404 = views.not_found_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("core.urls")),
    path('auth/', include("guardian.urls")),

    path('store/', include("core.urls")),
    path('store/auth/', include("guardian.urls")),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
]
