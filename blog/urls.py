from django.conf.urls import url
from django.views.generic import TemplateView
from blog import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^page/(?P<page>[0-9]*)$', views.home, name='home_page'),
    url(r'^posts/(?P<post_pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^create_post/$', views.create_post, name='create_post'),
    url(r'^posts/(?P<post_pk>[0-9]+)/update_post$', views.update_post, name='update_post'),
    url(r'^posts/(?P<post_pk>[0-9]+)/delete_post$', views.delete_post, name='delete_post'),
    url(r'^search/$', views.search, name='search'),
    url(r'^hide_comment/(?P<comment_pk>[0-9]+)$', views.hide_comment, name='hide_comment'),
    url(r'^about/$', TemplateView.as_view(template_name="blog/about.html"), name='about'),
]
