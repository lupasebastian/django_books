"""module defining form for creating new users"""
from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import atomic
from django.forms import CharField, Textarea

from .models import Profile


# pylint: disable=too-few-public-methods


class SignUpForm(UserCreationForm):
    """form defined for signing new user up"""
    class Meta(UserCreationForm.Meta):
        """class defining which fields from model should be included"""
        fields = ['username', 'first_name']

    information = CharField(label='Opowiedz parę słów o sobie i ulubionych '
                                  'książkach:', widget=Textarea, min_length=60)

    @atomic
    def save(self, commit=True):
        self.instance.is_active = False
        result = super().save(commit)
        information = self.cleaned_data['information']
        profile = Profile(information=information, user=result)
        if commit:
            profile.save()
        return result
