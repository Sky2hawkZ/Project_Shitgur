from django.shortcuts import render

def accmanage(request):
    return render(request, 'account_management/Account_management.html')
