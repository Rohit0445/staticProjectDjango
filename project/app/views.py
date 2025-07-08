from django.shortcuts import render
from .models import Student


# Create your views here.
def landingpage(req):
    return render(req,'landing.html')



def register(req):
    return render(req,'register.html',{'register':'register'})


def registerdata(req):
    # print('hello.....')
    # print(req.method)
    # print(req.POST)
    # print(req.FILES)
    if req.method=='POST':
        n=req.POST.get('name')
        e=req.POST.get('email')
        c=req.POST.get('number')
        p =req.POST.get('password')
        cp =req.POST.get('cpass')
        i=req.FILES.get('image')
        d=req.FILES.get('file')

        Student.objects.create(name=n,email=e,contact=c,image=i,document=d,password=p,cpass=cp)
        msg="registration data Saved"
        return render(req,'landing.html',{'msg':msg})


