from django.shortcuts import render, redirect
from .forms import RegistrationForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile


# Create your views here.
def register(request):
    if (request.method == 'POST'):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def public_profile(request, id):
    user_profile = Profile.objects.get(user_id=id)
    print(user_profile)
    return render(request, 'accounts/public_profile.html', {'user_profile': user_profile})          

@login_required
def update_profile(request):
    if (request.method == 'POST'):
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid:
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'accounts/update_profile.html', {'form': profile_form})