
from django.urls import path
from . import views
app_name = "users"
urlpatterns = [
    path('register/', views.Registration.as_view(), name='registration'),
    path('login/', views.NewLoginWiew.as_view(template_name="login.html", authentication_form="LoginForm"), name='login'),
    path('users/', views.UserListView.as_view(), name='user_list'),
]