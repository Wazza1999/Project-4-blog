from . import views
from django.urls import path, include
from .views import CategoryPostsListView, add_post, delete_post, edit_post

""" Walkthrough and custom url patterns """
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('category/<slug:category_slug>/', CategoryPostsListView.as_view(),
         name='category_posts'),
    path('add_post/', add_post, name='add_post'),
    path('post/<int:post_id>/delete/', delete_post, name='delete_post'),
    path('post/<int:post_id>/edit/', edit_post, name='edit_post'),
    path('summernote/', include('django_summernote.urls')),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]
