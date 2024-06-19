from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.register, name='register'),
    path('login', views.login_p, name='login'),
    path('blog', views.add_blog, name='blog'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('show_message/<slug:message_id>', views.show_message, name="show_message")
]
