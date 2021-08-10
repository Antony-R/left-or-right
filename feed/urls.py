from django.urls import path
from . import views
from .views import PostListView, CreatePostView, UpdatePostView, DeletePostView, LeftVote, RightVote, about_us, landing_page

urlpatterns = [
    #path('', views.home, name='home')
    path('', landing_page, name='landing_page'),
    path('home/', PostListView.as_view(), name='home'),
    path('create-post/', CreatePostView.as_view(), name='create_post'),
    path('post/<int:pk>/left-vote', LeftVote, name='left_vote_post'),
    path('post/<int:pk>/right-vote', RightVote, name='right_vote_post'),
    path('post/<int:pk>/update', UpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('about-us/', about_us, name='about_us'),
]
