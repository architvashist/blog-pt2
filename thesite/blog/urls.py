from django.urls import path,include
from . import views
from .views import DraftListView,AboutView,PostListView,PostDetailView,PostUpdateView,PostDeleteView,PostCreateView
from  django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('',PostListView.as_view(),name='post_list'),
    path('about/',AboutView.as_view(),name='about'),
    path('post/<int:pk>',PostDetailView.as_view(),name='post_detail'),
    path('post/new',PostCreateView.as_view(),name='post_create'),
    path('post/update/<int:pk>',PostUpdateView.as_view(),name='post_edit'),
    path('post/delete/<int:pk>',PostDeleteView.as_view(),name='post_remove'),
    path('draft/',DraftListView.as_view(),name='draft_list'),
    path('post/<int:pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/approve',views.approve_comment,name='comment_approve'),
    path('comment/<int:pk>/delete',views.comment_delete , name='comment_remove'),
    path('post/<int:pk>/publish',views.publish_post,name='post_publish'),
    path('login/',LoginView.as_view(template_name='blog/login.html'),name='login'),
    path('logout',LogoutView.as_view(),name='logout')
]
