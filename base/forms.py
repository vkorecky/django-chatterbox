from logging import getLogger

from django import forms
from django.core.exceptions import ValidationError
from django.forms import Form, Textarea, ModelForm

from base.models import Room

LOGGER = getLogger()


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['participants']

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 2:
            validation_error = "Name must contains min. 2 chars."
            LOGGER.warning(f'{name} : {validation_error}')
            raise ValidationError(validation_error)
        return name.capitalize()
