from django.contrib import messages
from order.forms import orderF
from django.shortcuts import redirect, render
from user.models import *
from user.forms import *
from stay.models import *
from order.models import *
# Create your views here.
def orderlistV(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        userip = x_forwarded_for.split(',')[0]
    else:
        userip = request.META.get('REMOTE_ADDR')
    userexist = user.objects.filter(usip = userip).exists()
    if userexist:
        cuser = user.objects.get(usip = userip)   
        orderexist = order.objects.filter(user = cuser).exists()
        if orderexist:
            corder = order.objects.get(user = cuser)
            context = {
                "usorder": stay.objects.all(),
                "order":corder,
                "form":orderF(),
            }
            return render(request, "order_list.html", context) 
        else:
            context = {
                "usorder": stay.objects.all(),
                "form":orderF(),
            }
            return render(request, "order_list.html", context)

    else:
        context = {
            "usorder": stay.objects.all(),
            "form":orderF(),
        }

        return render(request, "order_list.html", context)


def conforder(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        userip = x_forwarded_for.split(',')[0]
    else:
        userip = request.META.get('REMOTE_ADDR')

    cuser = user.objects.get(usip = userip)
    if request.method == "POST":
        fname = request.POST["fname"]
        mname = request.POST["mname"]
        lname = request.POST["lname"]
        usid = request.POST["usid"]
        usaddres = request.POST["usaddres"]
        usphone = request.POST["usphone"]
        totprc = request.POST["totprc"]
        if fname and mname and lname and usid and usaddres and usphone and totprc :
            orderexist = order.objects.filter(user = cuser).exists()
            stays = stay.objects.filter(ipuser = cuser)
            tot = 0
            for t in stays:
                tot = tot + t.totprice
            if int(totprc) == int(tot):
                if not orderexist:
                    det = stay.objects.filter(ipuser = cuser)
                    norder = order()
                    norder.user = cuser
                    norder.fname = fname
                    norder.mname = mname
                    norder.lname = lname
                    norder.idnumber = usid
                    norder.usaddres = usaddres
                    norder.usphone = usphone
                    norder.totprc = totprc
                    norder.save()
                    
                    oorder = order.objects.get(user = cuser)
                    for dets in det:
                        oorder.bdetail.add(dets)
                        oorder.save()
                    messages.success(request, "we did recieve your order and we will communicate with you soon, this your bill please save it with you thank you for using our site services")
                else:
                    det = stay.objects.filter(ipuser = cuser)
                    corder = order.objects.get(user = cuser)
                    corder.fname = fname
                    corder.mname = mname
                    corder.lname = lname
                    corder.idnumber = usid
                    corder.usaddres = usaddres
                    corder.usphone = usphone
                    corder.totprc = totprc
                    corder.save()
                    for dets in det:
                        corder.bdetail.add(dets)
                        corder.save()
                    messages.success(request, "we did recieve your order and we will communicate with you soon, this your bill please save it with you thank you for using our site services")
            else:
                messages.warning(request, "don't editing or coding again")
                return redirect("/orders/")
        else:
            messages.warning(request, "you missed some data please enter all data required")
            return redirect("/orders/")
    context={
        "dord":order.objects.get(user = cuser),
        "romord":order.objects.get(user = cuser).bdetail.all(),
    }
    return render(request, "conf.html", context)


