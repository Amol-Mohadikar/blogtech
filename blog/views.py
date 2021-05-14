from django.shortcuts import render,redirect
from django.http import HttpResponse, response
from .models import Blogpost
from .models import Mainblogpost
from .models import Message
import json
import requests

# Create your views here.


def index(request):
    
    myposts=Blogpost.objects.all()
    mainpost=Mainblogpost.objects.get(maintitle1="Technology")
    print(mainpost)

    # mainpost
    # print(myposts)
    # a=Blogpost.objects.get(tilte="Covid-19")
    # b=a.subtitle
    # params={'maintitle':"Technology"}
    return render(request,'blog/home.html',{'myposts':myposts,'mainpost':mainpost})

def blogpost(request,id):
    post = Blogpost.objects.filter(newpost_id=id)[0]
    # print(post)
    return render(request, 'blog/blogpost.html',{'post':post})


def contact(request):
    # post = Blogpost.objects.filter(newpost_id=id)[0]
    # print(post)
    if request.method =='POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        contactno = request.POST['contactno']
        message = request.POST['message']


        # recaptcha stuff
        # clientkey = request.POST['g-recaptcha-response']
        # secretkey='6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'
        # captchadata={
        #     'secret':secretkey,
        #     'response': clientkey
        # }
        # r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=captchadata)
        # response= json.loads(r.text)
        # verify = response['success']
        # print('your success is:',verify)
        # if verify:
            
        amol= Message(first_name=first_name,last_name=last_name,email=email,contactno=contactno,message=message)
        amol.save()
    
        return HttpResponse("<h1>Form Successfully Send :)</h1>  ")
        # else:
        #     return HttpResponse("<h1>Form not Send :(</h1>  ")
    else:

        return render(request, 'blog/contact.html')