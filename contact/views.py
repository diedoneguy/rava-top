from multiprocessing import context
from django.shortcuts import redirect, render
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .forms import ContactForm
from django.http import HttpResponse

def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'],
            to_email = form.cleaned_data['email'],
            message = form.cleaned_data['message']

            try:
                subject = f'Welcome to our restaraunt {name}'
                message = f'Thank you for Contact us {name}\n You are response is been noted\n We will contact you shortly '
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [to_email]
                send_mail(subject,message,email_from, recipient_list)
            except:
                return HttpResponse('invalid_data')
            
            return redirect('contact:send_email')
        else:
            form = ContactForm()

        context = {
            'form':form
        }
        return render(request, 'contact.html',context)
def send_success(request):
    return redirect(request,'contact.html')
