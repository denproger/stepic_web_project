from django.conf.urls import patterns, include, url
from qa.views import test
from qa.views_question import *
from qa.views_answer import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', get_new_questions, name="main"),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^question/(\d+)/', get_question, name="question"),
    url(r'^ask/', ask, name='ask'),
    url(r'^popular/', get_popular_questions, name="popular"),
    url(r'^new/', test),
    url(r'^answer/', add_answer, name='answer'),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

