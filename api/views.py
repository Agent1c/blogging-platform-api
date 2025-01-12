from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import BlogPost  # Import your BlogPost model
from .serializers import BlogPostSerializer  # Import your serializer

class BlogPostListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Retrieve all blog posts
        posts = BlogPost.objects.all()  # Query the BlogPost model
        
        # Serialize the posts
        serializer = BlogPostSerializer(posts, many=True)  # Use the serializer
        
        # Return the serialized data
        return Response({'posts': serializer.data})