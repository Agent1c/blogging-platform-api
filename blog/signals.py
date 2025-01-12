from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BlogPost

@receiver(post_save, sender=BlogPost)
def post_save_blog_post(sender, instance, created, **kwargs):
    if created:
        # Perform some action when a new BlogPost is created
        print(f'New blog post created: {instance.title}')