from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage


def pagrindinis(request):
    try:
       message = BaseEmailMessage(
           template_name='emails/triusis.html',
           context={'name': 'Dainius'}
       )
       message.send(['peredniokas23@gmail.com'])
    except BadHeaderError:
        pass
    return render(request, 'triusis.html', {'name': 'Dainius'})