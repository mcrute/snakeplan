import models
from django.forms import ModelForm


class StoryForm(ModelForm):

    class Meta:
        model = models.Story
        fields = ('project', 'name')
