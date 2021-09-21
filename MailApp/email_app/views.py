from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .forms import ContactForm
from .files import handle_uploaded_file
from django.core.mail import send_mail

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            subject = form.cleaned_data['subject']
            sep = form.cleaned_data['separator']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            recipients = open('temp_plik/name.txt', 'r').read().split(sep)
            recipients.append(sender)
            send_mail(subject, message, "emailapp.formularz@gmail.com", recipients)
        return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    return render(request, 'email_app/name.html', {'form': form})