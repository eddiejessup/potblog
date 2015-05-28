from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

accounts_urlpatterns = [
    url(r'^login/$', auth_views.login, name="login"),
    url(r'^logout/$', auth_views.logout, name="logout"),
]

urlpatterns = [
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include(accounts_urlpatterns, namespace="accounts")),
]
