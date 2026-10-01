from django.shortcuts import render

# Create your views here.
def index(request):

    empresa = ''
    context = {
        'lista': empresa
    }
    return render(request, "index.html", context)