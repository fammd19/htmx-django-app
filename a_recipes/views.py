from django.shortcuts import render
from django.forms import ModelForm
from .models import *

# Create your views here.
def home_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'a_recipes/home.html', {'recipes': recipes})

class RecipeCreateForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

def recipe_post_view(request):
    form = RecipeCreateForm()
    return render (request, 'a_recipes/recipe_create.html', {'form': form})
