from django.shortcuts import render
from django.http import JsonResponse
from .models import PasswordEntry

def password_manager(request):
    entries = PasswordEntry.objects.all()
    return render(request, 'password_manager_app/password_manager.html', {'entries': entries})

def add_password(request):
    if request.method == 'POST':
        website = request.POST.get('website', '')
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        if website and username and password:
            PasswordEntry.objects.create(website=website, username=username, password=password)
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})

