from django.shortcuts import redirect, render
from .forms import *
from home.models import *
from .models import *
from order.forms import *
from stay.models import *
# Create your views here.

def userv(request, id):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        userip = x_forwarded_for.split(',')[0]
    else:
        userip = request.META.get('REMOTE_ADDR')
    

    if request.method == 'POST':
        if user.objects.filter(usip=userip) or user.objects.filter():
            rom = roomM.objects.get(id=id)
            cuser=user.objects.get(usip=userip)
            cuser.usrobook.add(rom)
            rom.roavaliable = False
            rom.save()
            cuser.save()
            broom = user.objects.get(usip = userip).usrobook.get(id = id).roname
            bokrom = roomM.objects.get(roname = broom)
            price = bokrom.roprice
            oprice = bokrom.roomoldprice
            nstay = stay()
            nstay.ipuser = cuser
            nstay.brom = rom
            nstay.sroprice = price
            nstay.srooldprice = oprice
            nstay.stay = 1
            nstay.totprice = rom.roprice
            nstay.save()
            return redirect("/orders")
        else:
            rom = roomM.objects.get(id=id)
            cuser = user()
            cuser.usip = userip
            cuser.save()
            cuser=user.objects.get(usip=userip)
            cuser.usrobook.add(rom)
            rom.roavaliable = False
            cuser.save()
            rom.save()
            broom = user.objects.get(usip = userip).usrobook.get(id = id).roname
            bokrom = roomM.objects.get(roname = broom)
            price = bokrom.roprice
            oprice = bokrom.roomoldprice
            nstay = stay()
            nstay.ipuser = user.objects.get(usip = userip)
            nstay.brom = rom
            nstay.sroprice = price
            nstay.srooldprice = oprice
            nstay.stay = 1
            nstay.totprice = rom.roprice
            nstay.save()
            return redirect("/orders")
    context={
        "room":roomM.objects.get(id=id),
        "form":userf()
    }
    return render(request, "userf.html", context)



def DeletRoom(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        userip = x_forwarded_for.split(',')[0]
    else:
        userip = request.META.get('REMOTE_ADDR')
    if request.method == 'POST':
        rom = request.POST["rom"]
        if user.objects.filter(usip = userip).exists() and user.objects.get(usip = userip ).usrobook.filter(roname=rom).exists():
            cuser = user.objects.get(usip = userip)
            orderexist = order.objects.filter(user = cuser).exists()
            room = cuser.usrobook.get(roname = rom)
            roma = roomM.objects.get(roname = rom)
            scrom = stay.objects.get(brom = roma)
            roma.roavaliable = True
            scrom.delete()
            roma.save()
            cuser.usrobook.remove(room)
            if orderexist:
                det = stay.objects.filter(ipuser = cuser)
                corder = order.objects.get(user = cuser)
                tot = 0
                for dets in det:
                    tot = dets.totprice + tot
                corder.totprc = tot
                corder.save()
            else:
                pass
        else:
            return redirect("/orders/")
    if not stay.objects.filter(ipuser = cuser).exists():
        user.objects.get(usip = userip).delete()


    return redirect("/orders/")

def deletallroom(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        userip = x_forwarded_for.split(',')[0]
    else:
        userip = request.META.get('REMOTE_ADDR')

    userexist = user.objects.filter(usip = userip).exists()
    if userexist:
        cuser = user.objects.get(usip = userip)
        roms = cuser.usrobook.all()
        for rom in roms:
            rom.roavaliable = True
            rom.save()
        cuser.delete()
        return redirect("/orders/")