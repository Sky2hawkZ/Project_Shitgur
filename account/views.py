from django.shortcuts import render
from django.shortcuts import redirect 
from django.http import HttpResponseRedirect 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from account.models import user_data
from forms import UserDataForm

template_acc_name = 'account/Account_management.html'
template_acc_error_name = 'account/Account_management_error.html'
template_acc_success_name = 'account/Account_management_success.html'

template_logreg_name = 'account/reg_log-in_page.html'
template_logreg_error_name = 'account/reg_log-in_error.html'
template_logreg_success_name = 'account/reg_log-in_success.html'
template_logreg_updatepass_name = 'account/reg_log-in_updatepass.html'

def acclogreg(request):
    return render(request, template_logreg_name)

@login_required
def accmanage(request):
    return render(request, template_acc_name)

def authview(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password = password)
    if user:
        auth.login(request, user)
        return redirect('management')
    else:
        return render(request, template_logreg_error_name)

"""work in progress below this line"""

def register(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    password_repeat = request.POST.get('password_repeat', '')
    email = request.POST.get('email', '')
    dob = request.POST.get('dob', '')

    if request.user.is_authenticated():
        return redirect('management')
    else:
        if not User.objects.filter(username=username).exists() and username != "":
            user = User(username=username)
            User.email = email
            user_data.date_of_birth = dob
            if password == password_repeat and password != "":
                user.set_password(password)
            else:
                return render(request, template_logreg_error_name)
            user.is_active = True
            user.save()
            return render(request, template_logreg_success_name)
        else:
            return render(request, template_logreg_error_name)

@login_required
def update_password(request):
    current_password = request.POST.get('current_password', '')
    new_password = request.POST.get('new_password', '')
    repeat_password = request.POST.get('repeat_password', '')

    password_valid = request.user.check_password(current_password)
    if password_valid:
        if new_password == repeat_password:
            request.user.set_password(new_password)
            request.user.save()
            return render(request, template_logreg_updatepass_name)
        else:
            return render(request, template_acc_error_name)
    else:
        return render(request, template_acc_error_name)

@login_required
def update_user_info(request):
    first_name = request.POST.get('first_name', '')
    last_name = request.POST.get('last_name', '')
    gender = request.POST.get('gender', '')
    country = request.POST.get('country', '')
    date_of_birth = request.POST.get('date_of_birth', '')
    about = request.POST.get('about', '')

    if request.POST:
        form = UserDataForm(request.POST or None)
        if form.is_valid():
            user = form.save()

        User.first_name = first_name
        User.last_name = last_name
        user_data.gender = gender
        user_data.country = country
        user_data.date_of_birth = date_of_birth
        user_data.about = about

        if form.is_valid():
            form.save()
            return render(request, template_acc_success_name)
        else:
            return render(request, template_acc_error_name)

    else:
        return render(request, template_acc_error_name)

def fetch_user_data(request):
    data = user_data.objects.all()
    user = User.objects.all()
    context = {'users': users, 'data': data}
    return render(request, template_acc_name, context)