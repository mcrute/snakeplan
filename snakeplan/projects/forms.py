from django.forms import ModelForm

import models as project_models


class ProjectForm(ModelForm):

    class Meta:
        model = project_models.Project
