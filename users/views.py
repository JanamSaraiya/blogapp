from django.shortcuts import render, redirect
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save() # when you save this post_save signal invoke and create instance of profile model as well
            messages.success(
                request, f'Hey, {username}, your account has been created.')
            messages.info(request, f'Now you can login.')
            return redirect('login')
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


def profile(request, pk):
    prof = Profile.objects.get(pk=pk)
    context = {
        'prof': prof
    }
    return render(request, 'users/profile.html', context)


@login_required()
def profile_update(request):
    if request.method == 'POST':

        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            username = u_form.cleaned_data.get('username')
            u_form.save()
            p_form.save()
            messages.success(
                request, f'Hey, {username}, your information has been updated.')
            return redirect('profile-update')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile_update.html', context)
