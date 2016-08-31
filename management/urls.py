from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings
urlpatterns = [

url(r'^$', views.index, name='index'),
url(r'^signup/$', views.signup, name='signup'),
url(r'^login/$', views.login, name='login'),
url(r'^logout/$', views.logout, name='logout'),
url(r'^set_password/$', views.set_password, name='set_password'),
url(r'^add_book/$', views.add_book, name='add_book'),
url(r'^view_book_list/$', views.view_book_list, name='view_book_list'),
url(r'^add_img/$', views.add_img, name='add_img'),
url(r'^view_book_list/detail/$', views.detail, name='detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
