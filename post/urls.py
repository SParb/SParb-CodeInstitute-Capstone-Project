from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('createpost/', views.post_create, name='post_create'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<int:post_id>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('<int:post_id>/delete_post/', views.post_delete, name='post_delete'),
]