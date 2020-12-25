from django.contrib.auth.forms import UserCreationForm
from django.db.transaction import atomic
from django.forms import CharField, Textarea

from .models import Profile


class SignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'first_name']

    information = CharField(label='Opowiedz parę słów o sobie i ulubionych książkach:', widget=Textarea, min_length=60)

    @atomic
    def save(self, commit=True):
        self.instance.is_active = False
        result = super().save(commit)
        information = self.cleaned_data['information']
        profile = Profile(information=information, user=result)
        if commit:
            profile.save()
        return result
