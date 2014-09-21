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
    from PIL import Image as img
    import matplotlib.pyplot as mp
    # return_dict = {'numpy_array': np.arange(10)}
    i=img.open(os.path.join(settings.IMAGES_ROOT, 'images', "numbers", "y0.3.png"))
    iar=np.asarray(i)
    i2=img.open(os.path.join(settings.IMAGES_ROOT, 'images', "numbers", "y0.4.png"))
    iar2=np.asarray(i2)
    i3=img.open(os.path.join(settings.IMAGES_ROOT, 'images', "numbers", "y0.5.png"))
    iar3=np.asarray(i3)
    i4=img.open(os.path.join(settings.IMAGES_ROOT, 'images',  "sentdex.png"))
    iar4=np.asarray(i4)

    def threshold(arr):
        balance=[]
        newarr=arr
        for row in arr:
            for pix in row:
                avg=int(sum(pix[0:3])/3)
                balance.append(avg)
        bal=int(sum(balance)/len(balance))
        for r in newarr:
            for pixx in r:
                if int(sum(pixx[0:3])/3)>=bal:
                    pixx[0]=255
                    pixx[1]=255
                    pixx[2]=255
                    pixx[3]=255
                else:
                    pixx[0]=0
                    pixx[1]=0
                    pixx[2]=0
                    pixx[3]=255
        return newarr
    a=iar
    threshold(a)
    fig=mp.figure()
    ax1=mp.subplot2grid((8,8),(0,0),rowspan= 4,colspan=4)
    ax2=mp.subplot2grid((8,8),(4,0),rowspan= 4,colspan=4)
    ax3=mp.subplot2grid((8,8),(0,4),rowspan= 4,colspan=4)
    ax4=mp.subplot2grid((8,8),(4,4),rowspan= 4,colspan=4)
    ax1.imshow(iar)
    ax2.imshow(iar2)
    ax3.imshow(iar3)
    ax4.imshow(iar4)
    mp.show()

    return render_to_response(
        'nmp.html',
        locals(),
        context_instance=RequestContext(request, iar))



def register(request):
    return render_to_response(
        'register.html')