import re
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():                     #Save from SQL injection attack 
#             form.save
#     form = UserCreationForm()


def dashboard(request):
    return render(request, 'submissions/dashboard.html')