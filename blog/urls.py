from . import views
from django.urls import path
from .views import CategoryPostsListView, manage_posts


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('category/<slug:category_slug>/', CategoryPostsListView.as_view(),
         name='category_posts'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('manage_posts/', manage_posts, name='manage_posts'),
]
