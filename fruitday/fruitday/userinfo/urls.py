from django.conf.urls import url
from userinfo import views

urlpatterns = [
    url(r'^login',views.signin,name='login_in')
]