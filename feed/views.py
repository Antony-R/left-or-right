from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,  View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect, request
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
# def home(request):
#     posts = Post.objects.all()
#     context = {'posts': posts}
#     return render(request, 'feed/home.html', context)

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'feed/home.html'
    ordering = ['-datetime']

class CreatePostView(LoginRequiredMixin, CreateView):
    
    model = Post
    fields = ['title', 'left_title', 'left_content', 'right_title', 'right_content']
    success_url = '/home'

    def form_valid(self, form):
        form.instance.uname = self.request.user
        return super().form_valid(form)

class UpdatePostView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    
    model = Post
    fields = ['title', 'left_title', 'left_content', 'right_title', 'right_content']
    success_url = '/home'

    def form_valid(self, form):
        form.instance.uname = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if (post.uname == self.request.user):
            return True
        return False

class DeletePostView(LoginRequiredMixin, DeleteView, UserPassesTestMixin):
    
    model = Post
    success_url = '/home'

    def test_func(self):
        post = self.get_object()
        if (post.uname == self.request.user):
            return True
        return False

@login_required
def LeftVote(request, pk, *args, **kwargs):
    post = Post.objects.get(pk=pk)

    is_right_voted = False
    for vote in post.right_vote.all():
        if vote == request.user:
            is_right_voted = True
            break
    if is_right_voted:
        post.right_vote.remove(request.user)

    is_left_voted = False
    for vote in post.left_vote.all():
        if vote == request.user:
            is_left_voted = True
            break
    if not is_left_voted:
        post.left_vote.add(request.user)
    if is_left_voted:
        post.left_vote.remove(request.user)
    data = {
        "is_left_voted": not is_left_voted,
        "left_vote_count": post.left_vote.all().count(),
        "right_vote_count": post.right_vote.all().count(),
        "is_right_voted": is_right_voted  
    }
    return JsonResponse(data, safe=False)

@login_required
def RightVote(request, pk, *args, **kwargs):
    post = Post.objects.get(pk=pk)

    is_left_voted = False
    for vote in post.left_vote.all():
        if vote == request.user:
            is_left_voted = True
            break
    if is_left_voted:
        post.left_vote.remove(request.user)

    is_right_voted = False
    for vote in post.right_vote.all():
        if vote == request.user:
            is_right_voted = True
            break
    if not is_right_voted:
        post.right_vote.add(request.user)
    if is_right_voted:
        post.right_vote.remove(request.user)
    
    data = {
        "is_right_voted": not is_right_voted,
        "right_vote_count": post.right_vote.all().count(),
        "left_vote_count": post.left_vote.all().count(),
        "is_left_voted": is_left_voted 
    }
    return JsonResponse(data, safe=False)

def about_us(request):
    return render(request, 'feed/about-us.html')

def landing_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home')
    return render(request, 'feed/landing-page.html')