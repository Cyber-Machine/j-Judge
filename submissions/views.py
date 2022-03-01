import re
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():                     #Save from SQL injection attack 
            form.save()
            redirect('login')
    form = UserCreationForm()
    args = {
        'form': form,
    }
    return render(request, 'submissions/register.html',args)
  
def dashboard(request):
    return render(request, 'submissions/dashboard.html')