from django import forms

from notes.notes_app.models import Profile, Note


class CreateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(CreateProfileForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Profile
        fields = '__all__'


class CreateNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(CreateNoteForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url',)


class EditNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(EditNoteForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url',)


class DeleteNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(DeleteNoteForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url',)


class DetailsNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'image_url', 'content',)
