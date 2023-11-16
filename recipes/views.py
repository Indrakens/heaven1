from django.shortcuts import render, get_object_or_404
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


class RecipeDetail(View):
    """
    Displays cocktail recipe details for logged-in users
    Logged users can like and leave a comment
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        cocktail = get_object_or_404(queryset, slug=slug)
        comments = cocktail.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if cocktail.likes.filter(id=self.request.user.id).exists():
            liked = True 

        return render(
            request,
            "recipe.html",
            {
                "cocktail": cocktail,
                "commented": False, 
                "liked": liked,
            },
        )       
