from django.urls import path, re_path
from . import views

urlpatterns = [
    # path( url/, view, kwargs(key word arguments), name)
    path('', views.index, name='index'),
    # re_path(r'^([0-9]+)/$', views.show, name='show'),  # using RegEx
    path('<int:dog_id>/', views.show, name='show'),
    path('post_dog/', views.post_dog, name='post_dog'),
    path('user/<user_name>', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('like_dog/', views.like_dog, name='like_dog')
]
