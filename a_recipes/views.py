from django.shortcuts import render, redirect
from django.forms import ModelForm
from .models import *
from django import forms

# Create your views here.
def home_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'a_recipes/home.html', {'recipes': recipes})

class RecipeCreateForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'summary' : forms.Textarea(attrs={'rows':1, 'placeholder':'Add a summary...'}),
        }

def recipe_post_view(request):
    form = RecipeCreateForm()

    if request.method == 'POST':
        form = RecipeCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render (request, 'a_recipes/recipe_create.html', {'form': form})
