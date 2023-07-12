from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from .models import Book
from .serializers import BookSerializer
from rest_framework.exceptions import PermissionDenied
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        book = self.get_object()
        if book.author != request.user:
            raise PermissionDenied("You do not have permission to update this book.")
        return super().put(request, *args, **kwargs)

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        book = self.get_object()
        if book.author != request.user:
            raise PermissionDenied("You do not have permission to delete this book.")
        return super().delete(request, *args, **kwargs)


