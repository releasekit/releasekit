from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^webhook', include('webhook.urls')),
    url(r'^admin/', admin.site.urls),
]
