from operator import imod
import re
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from submissions.models import Submission
from submissions.forms import AddMarksForm, AddSubmissionForm
from django.contrib.auth.models import User
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
    submissions = Submission.objects.all()
    args = {
        'submissions': submissions,
    }
    if request.user.is_superuser:
        return render(request, 'submissions/admin_dashboard.html' , args)
    else:
        submission = Submission.objects.filter(user=request.user).first()
        args={
            'submission':submission
        }
        return render(request, 'submissions/student_dashboard.html',args)

def add_submission(request):
    if request.method == 'POST':
        form = AddSubmissionForm(request.POST)
        if form.is_valid():                     #Save from SQL injection attack 
            s = form.save(commit=False)     # Does Not Write to the Database.
            s.user = User.objects.get(id-request.user.id)
            s.save()
            redirect('dashboard')
    else:
            form=AddSubmissionForm()
    args = {
        'form': form,
    }
    return render(request, 'submissions/add_submission.html',args)