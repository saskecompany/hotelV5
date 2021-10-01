from django.shortcuts import redirect, render
from .models import *
from reviews.models import *
from reviews.forms import *
from django.contrib import messages
from user.models import user
from order.models import order
# Create your views here.

# forms save 
def servicesV(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    if request.method == 'POST':
        add_re = reF(request.POST, request.FILES)
        if add_re.is_valid():
            add_re.save()
            messages.success(request, "your rate published Successfully")
            return redirect('revs/')
        else:
            messages.warning(request, "sory we exist something wrong can you try again ")
    userexist = user.objects.filter(usip = ip).exists()
    if userexist:
        cuser = user.objects.get(usip = ip)
        orderexist = order.objects.filter(user = cuser).exists()
        if orderexist:
            uord = order.objects.get(user = cuser)
            context={
                'servs' : serviceM.objects.all(),
                'rooms' : roomM.objects.all(),
                'res' : reM.objects.all(),
                'ref' : reF(),
                "user": user.objects.filter(usip=ip),
                "order" : uord,
                }
        else:
            context={
            'servs' : serviceM.objects.all(),
            'rooms' : roomM.objects.all(),
            'res' : reM.objects.all(),
            'ref' : reF(),
            "user": user.objects.filter(usip=ip),
            }
    else:
        context={
        'servs' : serviceM.objects.all(),
        'rooms' : roomM.objects.all(),
        'res' : reM.objects.all(),
        'ref' : reF(),
        "user": user.objects.filter(usip=ip),
        }
    
    return render(request, "mpages/index.html", context)

def allservices(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    userexist = user.objects.filter(usip = ip).exists()
    if userexist:
        cuser = user.objects.get(usip = ip)
        orderexist = order.objects.filter(user = cuser).exists()
        if orderexist:
            uord = order.objects.get(user = cuser)
            context={
                "servs":serviceM.objects.all(),
                "user": user.objects.filter(usip=ip),
                "order" : uord,
                }
        else:
            context={
                "servs":serviceM.objects.all(),
                "user": user.objects.filter(usip=ip),
            }
    else:
        context={
        "servs":serviceM.objects.all(),
        "user": user.objects.filter(usip=ip),
    }
    return render(request, "allservices.html", context)

def allrooms(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    search = roomM.objects.all()
    name = None
    if "search_room" in request.GET:
        name = request.GET["search_room"]
        if name:
            search = search.filter(roname__icontains=name)
    userexist = user.objects.filter(usip = ip).exists()
    if userexist:
        cuser = user.objects.get(usip = ip)
        orderexist = order.objects.filter(user = cuser).exists()
        if orderexist:
            uord = order.objects.get(user = cuser)
            context={
                "rooms":search,
                "user": user.objects.filter(usip=ip),
                "order" : uord,
                }
        else:
            context={
                "rooms":search,
                "user": user.objects.filter(usip=ip),
            }
    else:
        context={
                "rooms":search,
                "user": user.objects.filter(usip=ip),
            }
    return render(request, "allrooms.html", context)

def roomdetailsV(request, slug):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    userexist = user.objects.filter(usip = ip).exists()
    if userexist:
        cuser = user.objects.get(usip = ip)
        orderexist = order.objects.filter(user = cuser).exists()
        if orderexist:
            uord = order.objects.get(user = cuser)
            context={
                "user": user.objects.filter(usip=ip),
                "romdet": roomM.objects.get(roslug=slug),
                "order" : uord,
                }
        else:
            context={
                "user": user.objects.filter(usip=ip),
                "romdet": roomM.objects.get(roslug=slug)
            }
    else:
        context={
                "user": user.objects.filter(usip=ip),
                "romdet": roomM.objects.get(roslug=slug)
            }
    return render(request, "romdet.html", context)


def allerv(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    userexist = user.objects.filter(usip = ip).exists()
    if userexist:
        cuser = user.objects.get(usip = ip)
        orderexist = order.objects.filter(user = cuser).exists()
        if orderexist:
            uord = order.objects.get(user = cuser)
            context={
                "res":reM.objects.all(),
                "user": user.objects.filter(usip=ip),
                "order" : uord,
                }
        else:
            context={
                "res":reM.objects.all(),
                "user": user.objects.filter(usip=ip),
            }
    else:
        context={
                "res":reM.objects.all(),
                "user": user.objects.filter(usip=ip),
            }
    return render(request, "allrev.html", context)

def servicesdetails(request, id):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    serv = serviceM.objects.get(id=id)
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
        userexist = user.objects.filter(usip = ip).exists()
    if userexist:
        cuser = user.objects.get(usip = ip)
        orderexist = order.objects.filter(user = cuser).exists()
        if orderexist:
            uord = order.objects.get(user = cuser)
            context={
                "serv" : serv,
                "order" : uord,
                }
        else:
            context={
                "serv" : serv,
            }
    else:
        context={
                "serv" : serv,
            }
    return render(request, "servdet.html", context)