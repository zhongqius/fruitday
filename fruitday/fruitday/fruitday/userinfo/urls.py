from django.conf.urls import url
from userinfo import views

urlpatterns = [
    url(r'^login', views.signin, name='login'),
    url(r'^loginin', views.login_, name='login_in'),
    url(r'^register', views.register, name='register')
]
