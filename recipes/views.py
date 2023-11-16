from django.shortcuts import render
from django.views import generic, View
from .models import Recipe


class RecipeList(generic.ListView):
    """
    Displays header and most recent added cocktails
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
