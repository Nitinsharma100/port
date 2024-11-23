from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
# Create your views here.
def home(request):
    return render(request,'app/home.html')
def about(request):
    return render(request,'app/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        phonenumber = request.POST.get('number')
        description = request.POST.get('desc')
        print({'name':name,'phonenumber':phonenumber,'desc':description})
        query = Contact(name=name, phonenumber=phonenumber, description=description)
        query.save()
        messages.info(request, f'The name is {name},  your number is {phonenumber}, and your query is {description}.')
        messages.success(request, 'We will get back to you soon.')

        return redirect('contact')

    return render(request, 'app/contact.html')


def projects(request):
    return render(request, 'app/blog.html')



