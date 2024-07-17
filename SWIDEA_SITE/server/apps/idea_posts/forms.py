from django import forms
from .models import IdeaPost
from apps.devtool_posts.models import DevtoolPost

class IdeaPostForm(forms.ModelForm):
  devtools = forms.ModelChoiceField(queryset=DevtoolPost.objects.all(), widget=forms.Select, label="예상 개발툴")
  class Meta():
    model = IdeaPost
    fields = '__all__'
    # ['title', 'content', 'devtools', 'interest', 'image', 'created_date', 'updated_date']