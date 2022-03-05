from django.forms import ModelForm
from submissions.models import Submission

class AddSubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['url']

class AddMarksForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['marks']