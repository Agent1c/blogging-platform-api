from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blog.views import home, about
from users.views import  profile_view

# app_name = 'blog' 

urlpatterns = [
       path('admin/', admin.site.urls),
       path('', home, name='home'),
       path('blog/', include('blog.urls', namespace='blog')),
       path('users/', include('users.urls')),
       path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
       path('profile/', profile_view, name='profile'),
       path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
       path('about/', about, name='about'),
   ]