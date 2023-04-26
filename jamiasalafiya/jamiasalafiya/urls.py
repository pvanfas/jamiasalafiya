from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("", include("web.urls", namespace="web")),
        path("academics/", include("academics.urls", namespace="academics")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)


admin.site.site_header = "Jamia Salafiya Administration"
admin.site.site_title = "Jamia Salafiya Admin Portal"
admin.site.index_title = "Welcome to Jamia Salafiya Admin Portal"
