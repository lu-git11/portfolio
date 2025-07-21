from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def AboutPage(request):
    return render(request, 'pages/about.html')

def ExperiencePage(request):
    return render(request, 'pages/experience.html')

def ContactPage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            message_body = (
                f"You have an email \n"
                f"Name: {name}\n"
                f"Email: {email}\n"
                f"Message: {message}\n"
            )

            try:
                send_mail(
                    "Email from portfolio page",
                    message_body,
                    email,
                    ['lullenj@gmail.com']                    

                )
                form = ContactForm()
                return render(request, 'pages/contact.html', {'form': form})
            except Exception as e:
                print(f"error sending email")
                return render(request, 'pages/contact.html', {'form': form,'error': str(e),})
                
        else:
            print("Invalid data")
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})