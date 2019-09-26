from django.shortcuts import render, redirect
from accounts.forms import (
    RegistrationForm,
    EditProfileForm,
    EditDetailedProfileForm
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile



@login_required
def home (request):
    args={}
    return render(request, 'accounts/home.html', args)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/login')
            return redirect('/accounts/edit_detailed_profile.html')

    else:
        form = RegistrationForm()
        args = {'form':form}
        return render(request, 'accounts/reg_form.html', args)

@login_required
def view_profile(request):
    args = {'user':request.user}
    return render(request, 'accounts/profile.html', args)
    
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    
    else:
        form = EditProfileForm(instance=request.user)
        args={'form':form}
        return render(request, 'accounts/edit_detailed_profile.html', args)

@login_required
def edit_detailed_profile(request):
    if request.method == 'POST':
        form = EditDetailedProfileForm(request.POST, instance=request.user.userprofile)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    
    else:
        form = EditDetailedProfileForm(instance=request.user.userprofile)
        args={'form':form}
        return render(request, 'accounts/edit_detailed_profile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data= request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,  form.user)
            return redirect('/account/profile')
        else:
            return redirect('/account/change-password')
    
    else:
        form = PasswordChangeForm(user=request.user)

        args={'form':form}
        return render(request, 'accounts/change_password.html', args)
