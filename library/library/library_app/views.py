from django.shortcuts import render, redirect

from library.library_app.forms import CreateProfileForm, CreateBookForm, EditBookForm, EditProfileForm, \
    DeleteProfileForm
from library.library_app.models import Profile, Book


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    books = Book.objects.all()
    context = {
        'books': books,
        'profile': profile
    }
    return render(request, 'home-with-profile.html', context)


def create_book(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')
    form = CreateBookForm()
    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    profile = get_profile()
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show home')
    form = EditBookForm(instance=book)
    context = {
        'form': form,
        'book': book,
        'profile': profile
    }
    return render(request, 'edit-book.html', context)


def show_details(request, pk):
    book = Book.objects.get(pk=pk)
    profile = get_profile()
    context = {
        'book': book,
        'profile': profile,
    }
    return render(request, 'book-details.html', context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('show home')


def show_profile(request):
    profile = get_profile()
    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context)


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


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show profile')
    form = EditProfileForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show home')
    form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'delete-profile.html', context)



