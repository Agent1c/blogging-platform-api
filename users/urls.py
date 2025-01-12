from django.urls import path
from django.contrib.auth import views as auth_views
from .views import  register, profile_view

urlpatterns = [
    # path('', UserListCreateView.as_view(), name='user-list-create'),  # No 'users/' prefix here
    # path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', profile_view, name='profile'),
]