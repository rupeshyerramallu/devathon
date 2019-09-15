from django.conf.urls import url
from . import views
app_name='home'
urlpatterns = [

    url(r'index', views.index, name='login'),
    url(r'login', views.log , name='login'),
    url(r'signin', views.signin , name='signin'),
    url(r'register', views.register, name='register'),
    url(r'inout', views.inout, name='inout'),
    url(r'adview', views.adview, name='adview'),
    url(r'logout', views.log_out, name='logout'),

]