from django.shortcuts import get_object_or_404, render, get_list_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.utils import timezone
from django.views.decorators.cache import cache_page
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.utils.http import url_has_allowed_host_and_scheme 
import logging
from blog.forms import CommentForm, UserRegistrationForm
from blog.models import BlogPost, Comment

logger = logging.getLogger(__name__)

def rate_limit(key_prefix, limit=5, period=60):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            key = f"{key_prefix}_{request.META.get('REMOTE_ADDR')}"
            attempts = cache.get(key, 0)
            if attempts >= limit:
                logger.warning(f"Rate limit exceeded for IP: {request.META.get('REMOTE_ADDR')}")
                raise PermissionDenied("Too many attempts. Please try again later.")
            cache.set(key, attempts + 1, period)
            return func(request, *args, **kwargs)
        return wrapper
    return decorator

@require_http_methods(["GET", "POST"])
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)  # Use the custom registration form
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('profile')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@rate_limit('login', limit=5, period=300)
@require_http_methods(["GET", "POST"])
def login_user_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next')
            if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts=None):
                return redirect(next_url)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})

@login_required  # Ensure only logged-in users can access the profile page
def profile_view(request):
    try:
        user_posts_count = BlogPost.objects.filter(author=request.user).count()
        last_post_date = BlogPost.objects.filter(author=request.user).order_by('-created_at').first()
        comments_count = Comment.objects.filter(author=request.user).count()
        
        user_data = {
            'user': request.user,
            'profile': getattr(request.user, 'profile', None),
            'last_login': request.session.get('last_login', 'First visit'),
            'user_posts_count': user_posts_count,
            'last_post_date': last_post_date.created_at if last_post_date else None,
            'comments_count': comments_count,
        }
        return render(request, 'users/profile.html', user_data)
    except Exception as e:
        logger.error(f"Error in profile view for user {request.user.username}: {str(e)}")
        messages.error(request, 'An error occurred while loading your profile.')
        return redirect('home')

def post_detail_view(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    comments = post.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    })

@require_http_methods(["POST"])
def logout_view(request):
    try:
        username = request.user.username
        logout(request)
        logger.info(f"User logged out: {username}")
        messages.success(request, 'You have been successfully logged out.')
    except Exception as e:
        logger.error(f"Error during logout: {str(e)}")
    return redirect('login')