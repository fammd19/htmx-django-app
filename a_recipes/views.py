from django.shortcuts import render

# Create your views here.
def home_view(request):
    title = "Fi's Recipes"
    return render(request, 'a_recipes/home.html',{'title': title})