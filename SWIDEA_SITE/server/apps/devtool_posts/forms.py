from django import forms
from .models import DevtoolPost

class DevtoolPostForm(forms.ModelForm):
  class Meta():
    model = DevtoolPost
    fields = ['name', 'kind', 'content']