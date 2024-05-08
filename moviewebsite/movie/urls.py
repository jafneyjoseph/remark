from django.urls import path
from . import views

app_name='movie'
urlpatterns = [
  path('',views.index,name='index'),
  path('admin_panel/', views.admin_panel, name='admin_panel'),
  path('add_category/', views.add_category, name='add_category'),
  path('movie/<int:movie_id>/',views.detail,name='detail'),
  path('add/',views.addmovie,name='addmovie'),
  path('update/<int:id>/', views.update, name='update'),
  path('delete/<int:id>/', views.delete, name='delete'),
  path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
  path('profile/', views.view_profile, name='view_profile'),
  path('profile/edit/', views.edit_profile, name='edit_profile'),

]

