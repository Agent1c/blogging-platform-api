# from django.urls import path
# from .views import (
#     create_post,
#     post_list,
#     update_post,
#     delete_post,
#     posts_by_category,
#     posts_by_author,
#     search_posts,
#     BlogListView,
#     BlogDetailView,
# )

# app_name = 'blog'

# urlpatterns = [
#     path('', BlogListView.as_view(), name='post_list'),
#     path('', post_list, name='post_list'),
#     path('post/<int:pk>/', BlogDetailView.as_view(), name='post_form'),
#     path('author/<str:author_username>/', posts_by_author, name='posts_by_author'),
#     path('category/<str:category_name>/', posts_by_category, name='posts_by_category'),
#     path('post/blog/new/', create_post, name='create_post'),
#     path('post/<int:pk>/edit/', update_post, name='update_post'),
#     path('post/<int:pk>/delete/', delete_post, name='delete_post'),
#     path('search/', search_posts, name='search_posts'),
# ]

from django.urls import path
from .views import (
       create_post,
       BlogListView,
       update_post,
       delete_post,
       posts_by_category,
       posts_by_author,
       search_posts,
       BlogDetailView,
   )

app_name = 'blog'

urlpatterns = [
       path('', BlogListView.as_view(), name='post_list'),  # Keep this line
       path('post/<int:pk>/', BlogDetailView.as_view(), name='post_form'),
       path('author/<str:author_username>/', posts_by_author, name='posts_by_author'),
       path('category/<str:category_name>/', posts_by_category, name='posts_by_category'),
       path('post/new/', create_post, name='create_post'),
       path('post/<int:pk>/edit/', update_post, name='update_post'),
       path('post/<int:pk>/delete/', delete_post, name='delete_post'),
       path('search/', search_posts, name='search_posts'),
   ]