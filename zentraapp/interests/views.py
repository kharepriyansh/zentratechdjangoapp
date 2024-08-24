from django.shortcuts import render, redirect,get_object_or_404
from .models import Interest
from users.models import User
from django.contrib import messages
from users.views import allusers,loginuser

# Create your views here.
def sendinterest(request,id):
    user_id = request.session.get('user_id')
    if user_id:
        receiver = User.objects.get(id=int(id))
        objuser=User.objects.get(id=int(user_id))
        if request.method =="POST" and receiver:
            message = "send a friend request"
            interest = Interest(sender=objuser, receiver=receiver, message=message)
            interest.save()
            messages.success(request, f'interest from {objuser.name} to {receiver.name} sent successfully')
            return redirect('allusers')
        return redirect('allusers')
    else:
        return redirect('loginuser')


def myrequests(request):
    user_id = request.session.get('user_id')
    if user_id:
        objuser=User.objects.get(id=int(user_id))
        all=Interest.objects.filter(receiver=objuser)
        requests={
            'requests':all
        }

        return render(request,'myrequests.html',{'requests':all})
    else:
        return redirect('allusers')