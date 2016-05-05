from django.conf.urls import include, patterns, url
from django.conf import settings
from django.contrib import admin

from projectapps.web import urls as web_urls


urlpatterns = [
    # For custom admins CMS's use:
    # url(r'^admin/', include(coreadmin_urls)),
    # url(r'^contrib-admin/', include(admin.site.urls)),

    # Contrib admin
    url(r'^admin/', include(admin.site.urls)),

    # Front-end
    url(r'', include(web_urls)),
]

if settings.DEBUG:
    # Serve static files on debug mode
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()

    # Enable API documentation and debugging tools
    if 'rest_framework_swagger' in settings.INSTALLED_APPS:
        urlpatterns += patterns('',
            url(r'^api-docs/', include('rest_framework_swagger.urls'))
        )
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns += patterns('',
            url(r'^__debug__/', include(debug_toolbar.urls)),
        )
