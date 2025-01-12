from rest_framework import serializers
from .models import BlogPost, Category, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = BlogPost
        # fields = ['id', 'title', 'content', 'author', 'category', 'published_date', 'tags', 'created_date']
        fields = ['id', 'title', 'content', 'author', 'created_at', 'published_date']  
        read_only_fields = ['published_date', 'created_date']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        blog_post = BlogPost.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(**tag_data)
            blog_post.tags.add(tag)
        return blog_post

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.category = validated_data.get('category', instance.category)
        instance.save()

        instance.tags.clear()
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            instance.tags.add(tag)
        return instance

