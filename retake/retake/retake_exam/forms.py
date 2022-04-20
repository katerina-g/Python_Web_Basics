from django import forms

from retake.retake_exam.models import Profile, Game


class CreateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')

        labels = {
            'email': 'Email',
            'age': 'Age',
            'password': 'Password'
        }
        widgets = {
            'password': forms.PasswordInput,
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password', 'first_name', 'last_name', 'profile_picture')

        labels = {
            'email': 'Email',
            'age': 'Age',
            'password': 'Password',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture'
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        games = Game.objects.all()
        games.delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'category', 'rating', 'max_level', 'image_url', 'summary')

        labels = {
            'title': 'Title',
            'category': 'Category',
            'rating': 'Rating',
            'max_level': 'Max Level',
            'image_url': 'Image URL',
            'summary': 'Summary'
        }


class EditGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'category', 'rating', 'max_level', 'image_url', 'summary')

        labels = {
            'title': 'Title',
            'category': 'Category',
            'rating': 'Rating',
            'max_level': 'Max Level',
            'image_url': 'Image URL',
            'summary': 'Summary'
        }


class DeleteGameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Game
        fields = ('title', 'category', 'rating', 'max_level', 'image_url', 'summary')

        labels = {
            'title': 'Title',
            'category': 'Category',
            'rating': 'Rating',
            'max_level': 'Max Level',
            'image_url': 'Image URL',
            'summary': 'Summary'
        }