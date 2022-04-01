from django.shortcuts import render, redirect

from notes.notes_app.forms import CreateProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm
from notes.notes_app.models import Profile, Note


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    notes = Note.objects.all()
    context = {
        'notes': notes,
        'profile': profile,
    }
    return render(request, 'home-with-profile.html', context)


def create_note(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')

    form = CreateNoteForm()
    context = {
        'form': form,
        'profile': profile,
        'no_note': True,
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    profile = get_profile()
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('show home')
    form = EditNoteForm(instance=note)
    context = {
        'form': form,
        'note': note,
        'profile': profile,
    }
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    profile = get_profile()
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('show home')
    form = DeleteNoteForm(instance=note)
    context = {
        'form': form,
        'note': note,
        'profile': profile,
    }
    return render(request, 'note-delete.html', context)


def show_details(request, pk):
    note = Note.objects.get(pk=pk)
    profile = get_profile()
    notes = Note.objects.all()
    context = {
        'note': note,
        'notes': notes,
        'profile': profile,
    }
    return render(request, 'note-details.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')

    form = CreateProfileForm()
    context = {
        'form': form,
        }
    return render(request, 'home-no-profile.html', context)


def show_profile(request):
    profile = get_profile()
    notes = Note.objects.all()
    notes_count = len(notes)
    context = {
        'profile': profile,
        'notes_count': notes_count,
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = get_profile()
    notes = Note.objects.all()
    profile.delete()
    notes.delete()
    return redirect('show home')
