from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate, login,logout
from home.models import *
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from home.models import *
from django.core.serializers import serialize
def home(req):
    login_status=0
    
    user_name='No login'
    email='No login'
    user_pro='NO login'
    village_name='NO logi'
    mandal='NO logi'
    district='NO logi'
    state='NO login'
    us=[]
    if req.user.is_authenticated:
        login_status=1
        user_name=req.user.username
        email=req.user.email
        user_pro=UserProfile.objects.get(user_id=req.user.id)
        village_name=user_pro.v_name 
        mandal=user_pro.mandal
        district=user_pro.dist
        state=user_pro.sta
        user_req=food_req.objects.filter(user_id=req.user.id)
        
        k={}
        for i in range(len(user_req)):
             k={}
             k['id']=user_req[i].id
             k['quantity'] =user_req[i].quantity
             k['image'] =str(user_req[i])
             k['city'] = user_req[i].city
             k['mandal'] = user_req[i].mandal 
             k['district'] =user_req[i].district
             k['state'] = user_req[i].state
             us.append(k) 
        
            
    return render(req,'index.html',{'login_status':login_status,'user_name':user_name,'email':email,'user_pro':user_pro,'village_name':village_name,'mandal':mandal,'district':district,'state':state,'user_req':us})
def create_user(req):
    if req.method=="POST":
         user_name=req.POST.get("u_name")
         email =req.POST.get("e_mail")  
         password=req.POST.get("password")    
         v_name=req.POST.get("v_name")
         mandal=req.POST.get("mandal")
         dist=req.POST.get("dist")
         sta=req.POST.get("sta")
         user_obj=User.objects.create(username=user_name, email=email, password=password)
         
         profile=UserProfile.objects.create(user=user_obj, v_name=v_name, mandal=mandal, dist=dist, sta=sta)
    return redirect('/home/a')
def login_c(req):
     
     if req.method=="POST":
        print("login")
        email =req.POST.get("email")  
        password=req.POST.get("password")
        print(email,password)
        User = get_user_model()
        try:
             user = User.objects.get(email=email) 
        except User.DoesNotExist:
            return HttpResponse("user not exist")
            #user = authenticate(req,email=email, password=password)
        
        print(user)
        if user is not None and user.password==password:
            # User authentication successful, log in the user
            login(req, user)
            return redirect('home')
        else:
            # Authentication failed
            return HttpResponse("Invalid login credentials")
        
     return redirect('/home/a')
def log_out(req):
    print("logout  called")
    logout(req)
    return redirect('/home/a')
def add_food(req):
    print("added food")
    user=req.user
    quantiy=req.POST.get("quantiy")
    image=req.FILES.get("image")
    
    cit=req.POST.get("cit")
    mand=req.POST.get("mand")
    dist=req.POST.get("dist")
    sta=req.POST.get("sta")
    food_request = food_req(
        user=user,
        quantity=quantiy,
        image=image,
        city=cit,
        mandal=mand,
        district=dist,
        state=sta
    )
    food_request.save()

    print(user,quantiy,image,cit,mand,dist,sta)
    return redirect('/home/a')
def bio_login(req):
    if req.method=="POST":
        email =req.POST.get("email")  
        password=req.POST.get("password")
        print(email,password)
        User = get_user_model()
        try:
             user = User.objects.get(email=email)
             
        except User.DoesNotExist:
            return HttpResponse("user not exist")
            #user = authenticate(req,email=email, password=password)
        
        print(user)
        if user is not None and user.password==password:
            # User authentication successful, log in the user
            login(req, user)
            return redirect('home')
        else:
            # Authentication failed
            return HttpResponse("Invalid login credentials")
        
       
    return render(req,'bio_login.html')