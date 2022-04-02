from django.shortcuts import render, redirect

from recipes.recipes_app.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from recipes.recipes_app.models import Recipe


def show_home(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = CreateRecipeForm()
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = EditRecipeForm(instance=recipe)
    context = {
        'form': form,
        'recipe': recipe
    }
    return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('show home')
    form = DeleteRecipeForm(instance=recipe)
    context = {
        'form': form,
        'recipe': recipe
    }
    return render(request, 'delete.html', context)


def show_details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    recipe_ingredients = recipe.ingredients.split(', ')
    context = {
        'recipe': recipe,
        'recipe_ingredients': recipe_ingredients
    }
    return render(request, 'details.html', context)



