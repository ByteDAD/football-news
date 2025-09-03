from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406432633',
        'name': 'Dimas Abyan Diasta',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
# Create your views here.
