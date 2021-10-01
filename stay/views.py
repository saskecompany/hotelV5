from django.shortcuts import redirect, render
from user.models import *
from user.forms import *
from stay.models import *

# Create your views here.

def longstay(request, id):
    if request.method == "POST":
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            userip = x_forwarded_for.split(',')[0]
        else:
            userip = request.META.get('REMOTE_ADDR')

        cuser = user.objects.get(usip = userip)
        broom = user.objects.get(usip = userip).usrobook.get(id = id).roname
        bokrom = roomM.objects.get(roname = broom)
        cromexist = stay.objects.filter(brom = bokrom).exists()

        q = request.POST['q']
        dt = request.POST['dt']
        price = bokrom.roprice
        oprice = bokrom.roomoldprice 
        tot = (int(q) * int(price))
        if int(q) <= 0:
            q = 1
        if tot <= 0: 
            tot = price
        if q and tot:
            if cuser.usip == userip:
                if not cromexist:
                    nstay = stay()
                    nstay.ipuser = cuser
                    nstay.brom = bokrom
                    nstay.stay = q
                    nstay.totprice = tot
                    nstay.books = dt
                    nstay.save()
                else:
                    csrom = stay.objects.get(brom = bokrom)
                    csrom.stay = q
                    csrom.totprice = tot
                    csrom.books = dt
                    csrom.save()

    return redirect("/orders/")