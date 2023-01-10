
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views import defaults
from guardian import views

defaults.page_not_found = views.not_found_view
handler404 = views.not_found_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("core.urls")),
    path('auth/', include("guardian.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
