from django.shortcuts import render

# Create your views here.
def AboutPage(request):
    return render(request, 'pages/about.html')

def ExperiencePage(request):
    return render(request, 'pages/experience.html')

def ContactPage(request):
    return render(request, 'pages/contact.html')