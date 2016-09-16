from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'untitle.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^board/$', 'main.views.board_index'),
    url(r'^(?P<pk>\d+)/$', 'main.views.post_detail', name='post_detail'),
    url(r'^(?P<pk>\d+)/comments/new/$', 'main.views.comment_new'),
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', 'main.views.comment_edit'),
    url(r'^(?P<pk>\d+)/edit/$', 'main.views.post_edit', name='post_edit'),
    url(r'^new/$', 'main.views.post_new'),
    url(r'^$', 'main.views.index'),
    url(r'^(?P<pk>\d+)/remove/$', 'main.views.post_remove', name='post_remove'),
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
