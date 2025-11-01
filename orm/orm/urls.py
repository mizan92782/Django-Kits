from django.contrib import admin
from django.urls import include, path
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls'))
]

# Include Debug Toolbar URLs only in DEBUG mode
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
