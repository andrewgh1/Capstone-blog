from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Tag, BlogPost, Comment
from blog.serializers import CategorySerializer, TagSerializer, BlogPostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from blog.permissions import IsAuthorOrReadOnly


# ViewSet for handling Category objects through the API.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()  # Defines the queryset to retrieve all Category objects
    serializer_class = CategorySerializer  # Specifies the serializer class for Category
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allows authenticated users to modify, but read-only for unauthenticated users


# ViewSet for handling Tag objects through the API.
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()  # Defines the queryset to retrieve all Tag objects
    serializer_class = TagSerializer  # Specifies the serializer class for Tag
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allows authenticated users to modify, but read-only for unauthenticated users


# ViewSet for handling BlogPost objects through the API.
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()  # Defines the queryset to retrieve all BlogPost objects
    serializer_class = BlogPostSerializer  # Specifies the serializer class for BlogPost
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]  # Custom permission: only the author can modify; others have read-only access

    # Add filtering options for search and ordering.
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]  # Enables search and ordering
    search_fields = ['title', 'content', 'author__username', 'tags__name']  # Searchable fields: title, content, author's username, and tags
    ordering_fields = ['published_date', 'category']  # Fields allowed for ordering: published date and category

    # Override the default create behavior to set the author of a BlogPost.
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Automatically sets the logged-in user as the author of the post

    # Custom action to filter blog posts by author.
    @action(detail=False) # Enables custom action to filter blog posts by author
    def by_author(self, request):
        author_username = request.query_params.get('username', None)  # Retrieve 'username' parameter from the request
        if author_username:
            posts = BlogPost.objects.filter(author__username=author_username)  # Filter blog posts by author
            serializer = BlogPostSerializer(posts, many=True)  # Serialize the filtered blog posts
            return Response(serializer.data)
        else:    # If no 'username' parameter is provided, return all blog posts
            serializer = self.get_serializer(posts, many=True)  # Serialize the filtered blog posts

        return Response(serializer.data)


# ViewSet for handling Comment objects through the API. 
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()  # Defines the queryset to retrieve all Comment objects
    serializer_class = CommentSerializer  # Specifies the serializer class for Comment
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]  # Custom permission: only the author can modify; others have read-only access     

    # Add filtering options for search and ordering.
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]  # Enables search and ordering
    search_fields = ['content', 'author__username', 'post__title']  # Searchable fields: content, author's username, and post's title
    ordering_fields = ['created_date']  # Fields allowed for ordering: created date


