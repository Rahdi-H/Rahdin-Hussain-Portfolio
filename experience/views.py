from django.shortcuts import render

# Create your views here.
def experience(request):
    return render(request, 'exp/exp.html')