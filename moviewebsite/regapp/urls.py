from .   import views
from django.urls import path

app_name='regapp'

urlpatterns = [

    path('register',views.register,name='register'),
    path("login",views.login,name='login'),
    path('logout',views.logout,name='logout')
]


