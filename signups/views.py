from django.conf import global_settings
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

from .forms import SignUpForm

# Create your views here.
#from skillshare import settings

def home(request):
    form = SignUpForm(request.POST or None)

    return render_to_response(
        'signup.html',
        locals(),
        context_instance=RequestContext(request))

def thankyou(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        subject = 'Thank you for your Pre-Order'
        message = 'Welcome to my site! We very much appreciate'
        from_email = global_settings.EMAIL_HOST_USER
        to_list = [save_it.email]
        send_mail(subject, message, from_email, to_list, fail_silently=False)
        messages.success(request, 'Thank you for your order!')
        return HttpResponseRedirect('/thank-you/')
    return render_to_response(
        'thankyou.html',
        locals(),
        context_instance=RequestContext(request))

def aboutus(request):
    return render_to_response(
        'aboutus.html',
        locals(),
        context_instance=RequestContext(request))

def nmp(request):
    import os
    import numpy as np
    from PIL import Image

    # return_dict = {'numpy_array': np.arange(10)}

    path = os.path.join(settings.IMAGES_ROOT, 'images', "dot.png")
    i = Image.open(path)
    iar = np.asarray(i)

    return render_to_response(
        'nmp.html',
        locals(),
        context_instance=RequestContext(request, iar))



def register(request):
    return render_to_response(
        'register.html')