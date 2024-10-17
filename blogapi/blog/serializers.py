from .models import BlogPost, Category,Tag,Comment
from django.contrib.auth import get_user_model
from rest_framework import serializers
from account.serializers import CustomUserSerializer

User = get_user_model()
#Serializing the Category model for API interactions.
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description'] # Specifies the fields to be serialized

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class BlogPostSerializer(serializers.ModelSerializer):

    author = CustomUserSerializer(read_only=True) # CustomUserSerializer is used for the nested author data (author details are read-only).
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)  # Many-to-many relationship

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'category', 'published_date', 'created_date', 'tags']

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'category', 'published_date', 'created_date','tags']
        read_only_fields = ['id', 'slug', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user  # Set the author from the request context
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('author', None)  # Ensure author can't be changed during the update
        return super().update(instance, validated_data)
    
class CommentSerializer(serializers.ModelSerializer):
    # ReadOnlyField ensures that the author field only displays the username, and cannot be changed via the API.
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_date']


'''
The CategorySerializer
Serializes the category ,model with  fields id, name, and description. This allows the API to send and receive category data in a structured format.

The TagSerializer
Serializes the Tag model with fields id and name. This is useful for managing tags associated with blog posts.

BlogPostSerializer:

Handles the serialization of the BlogPost model.
The author, category, and tags are nested serializers (CustomUserSerializer, CategorySerializer, and TagSerializer) to display their details in a structured format.
The author field is set to read-only and is automatically populated from the current request user when creating a blog post.
create() method ensures that the author of the blog post is set to the current logged-in user.
update() method prevents the author from being modified once the post is created.

CommentSerializer:

Serializes the Comment model with fields id, post, author, content, and created_date.
The author field is read-only and displays the username of the comment's author.'''