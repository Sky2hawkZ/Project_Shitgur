from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from account.models import user_data
from forms import UserDataForm
from forms import UserForm
from django.contrib.auth import logout


# Note to people messing around with the code: 

# in older version Management within authview/register was named 'management'
# accmanage was renamed to accmanage_regauth along with the url name change from management to Management

# variables to html pages have been altered aswell

# File locations set as variables due to frequent usage
account_management = 'account/Account_management.html'
account_error = 'account/Account_management_error.html'
account_success = 'account/Account_management_success.html'

logreg = 'account/reg_log-in_page.html'
logreg_error = 'account/reg_log-in_error.html'
logreg_success = 'account/reg_log-in_success.html'
logreg_updatepass = 'account/reg_log-in_updatepass.html'

# Render account login/registration page on request
def acclogreg(request):
    return render(request, logreg)

# Update user password and update page
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
            return render(request, logreg_updatepass)
        else:
            return render(request, account_error)
    else:
        return render(request, account_error)

# Update user profile and update page
@login_required
def update_user_info(request):
    user_form = UserForm(request.POST or None, request.FILES, instance=request.user)
    user_data_form = UserDataForm(request.POST or None, request.FILES, instance=request.user.user_data)

    if user_data_form.is_valid() and user_form.is_valid():
        user_data_form.save()
        user_form.save()
        return render(request, account_success, {
            'user_form': user_form,
            'user_data_form': user_data_form,
        })

    return render(request, account_management, {
        'user_form': user_form,
        'user_data_form': user_data_form,
    })

# Show user data on profile
def fetch_user_data(request):
    data = user_data.objects.all()
    user = User.objects.all()
    context = {'users': users, 'data': data}
    return render(request, account_management, context)

"""work in progress below this line"""

# Load forms and account management page, used in register and authview(log in)
@login_required
def accmanage_regauth(request):
    user_form = UserForm(instance=request.user)
    user_data_form = UserDataForm(instance=request.user.user_data)

    context = {'user_form': user_form, 'user_data_form': user_data_form}
    return render(request, account_management, context)


def logout_view(request):
    logout(request)
    return render(request, logreg)

# Create new user
def register(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    password_repeat = request.POST.get('password_repeat', '')
    email = request.POST.get('email', '')

    if request.user.is_authenticated():
        return redirect('Management')
    else:
        if not User.objects.filter(username=username).exists() and username != "":
            user = User(username=username)
            user.email = email
            if password == password_repeat and password != "":
                user.set_password(password)
            else:
                return render(request, logreg_error)
            user.is_active = True
            user.save()
            userdata = user_data(user=user)
            userdata.save()
            return render(request, logreg_success)
        else:
            return render(request, logreg_error)

# Log in for registered users
def authview(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password = password)
    if user:
        auth.login(request, user)
        return redirect('Management')
    else:
        return render(request, logreg_error)