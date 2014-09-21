from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^$', "signups.views.home", name='home'),
    url(r'^register/$', "signups.views.register", name='register'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^thank-you/$', "signups.views.thankyou", name='thankyou'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about-us/', "signups.views.aboutus", name='aboutus'),
    url(r'^test-numpy/', "signups.views.nmp", name='nmp'),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)