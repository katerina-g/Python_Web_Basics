from django.shortcuts import render, redirect

from retake.retake_exam.forms import CreateProfileForm, CreateGameForm, EditGameForm, DeleteGameForm, EditProfileForm, \
    DeleteProfileForm
from retake.retake_exam.models import Profile, Game


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_home(request):
    profile = get_profile()
    if profile:
        context = {
            'profile': profile,
        }
        return render(request, 'home-page.html', context)
    return render(request, 'home-page.html')


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show home')

    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'create-profile.html', context)


def profile_details(request):
    profile = get_profile()
    games = Game.objects.all()
    all_ratings = 0.0
    games_count = len(games)
    for g in games:
        all_ratings += g.rating
    if all_ratings > 0.0:
        avr_rating = all_ratings / games_count
    else:
        avr_rating = 0.0
    context = {
        'profile': profile,
        'games_count': games_count,
        'avr_rating': avr_rating,
    }
    return render(request, 'details-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
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


def show_dashboard(request):
    profile = get_profile()
    games = Game.objects.all()
    context = {
        'profile': profile,
        'games': games
    }
    return render(request, 'dashboard.html', context)


def create_game(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CreateGameForm()

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'create-game.html', context)


def game_details(request, pk):
    profile = get_profile()
    game = Game.objects.get(id=pk)
    context = {
        'game': game,
        'profile': profile
    }
    return render(request, 'details-game.html', context)


def game_edit(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditGameForm(instance=game)

    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'edit-game.html', context)


def game_delete(request, pk):
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DeleteGameForm(instance=game)

    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'delete-game.html', context)
