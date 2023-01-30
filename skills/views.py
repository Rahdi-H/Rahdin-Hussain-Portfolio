from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import Person
from django.contrib import messages

# Create your views here.

def skills(request):
    return render(request, 'skills/skills.html')

def django(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            Person(name=name, email=email, password=password).save()
            form = PersonForm()
            messages.add_message(request, messages.SUCCESS, 'Data successfully added')
    else:
        form = PersonForm()
    all_person = Person.objects.all()
    context = {
        'form' : form,
        'all_person' : all_person,
    }
    return render(request, 'skills/django.html', context)

def delete_data(request, id):
    a = Person.objects.get(pk=id)
    a.delete()
    return redirect('django')

def update_data(request, id):
    if request.method == 'POST':
        data = Person.objects.get(pk=id)
        form = PersonForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            # messages.add_message(request, messages.SUCCESS, 'Successfully updated')
            messages.success(request, 'Successfully updated')
    else:
        data = Person.objects.get(pk=id)
        form = PersonForm(instance=data)
    context = {
        'form' : form,
    }
    return render(request, 'skills/django_update.html', context)

def bootstrap(request):
    return render(request, 'skills/bootstrap.html')

def tailwindcss(request):
    return render(request, 'skills/tailwindcss.html')