from django.urls import path
from .views import ArticleListCreateAPIView, ArticleRetrieveUpdateDestroyAPIView, CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('article/', ArticleListCreateAPIView.as_view(), name='list-create-article'),
    path('article/<int:pk>/', ArticleRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-delete-article'),
    

    path('comments/', CommentListCreateAPIView.as_view(), name='list-create-comment'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-delete-comment'),
]