from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^posts/(?P<post_pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^create_post/$', views.create_post, name='create_post'),
    url(r'^posts/(?P<post_pk>[0-9]+)/update_post$', views.update_post, name='update_post'),
    url(r'^posts/(?P<post_pk>[0-9]+)/delete_post$', views.delete_post, name='delete_post'),
    url(r'^search/$', views.search, name='search'),
    url(r'^hide_comment/(?P<comment_pk>[0-9]+)$', views.hide_comment, name='hide_comment'),
]
