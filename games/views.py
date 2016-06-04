from django.shortcuts import render

#Render the recipe creation template and pass it the list of all recipes
def index(request):
    #if not request.user.is_authenticated():
    #   return redirect('/login')
    return render(request, 'games/index.html')
