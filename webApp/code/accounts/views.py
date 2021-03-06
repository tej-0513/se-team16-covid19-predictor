from django.shortcuts import render
from django.contrib.auth.models import auth,User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from accounts.models import ishospital,hospitalinfo
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
@csrf_exempt
def signup_hospital(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        hospitalname=request.POST['hospitalname']
        lastname=request.POST['lastname']
        pincode=request.POST['pincode']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        repassword=request.POST['repassword']

        if password != repassword:
            messages.info(request,'retyped password is not matching')
            return redirect('signup_hospital')


        query=User.objects.filter(username=username)
        if query.exists():
            messages.info(request,'User name already exists')
            return redirect('signup_hospital')
            # return HttpResponse("user already exist")


        entry=ishospital(username=username,hospital=True)
        entry.save()

        entry1=hospitalinfo(username=username,hospitalname=hospitalname,pincode=pincode)
        entry1.save()



        user=User.objects.create_user(username=username,email=email,password=password,first_name=firstname,last_name=lastname)
        user.save()
        
        messages.info(request,'User created!!!')
        return render(request,'signup_hospital.html')

        
    
    else:
        return render(request,'signup_hospital.html')


    

@csrf_exempt
def signup_government(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        repassword=request.POST['repassword']

        if password != repassword:
            messages.info(request,'retyped password is not matching')
            return redirect('signup_government')

        query=User.objects.filter(username=username)
        if query.exists():
            messages.info(request,'User name already exists')
            return redirect('signup_government')
            # return HttpResponse("user already exist")

        entry=ishospital(username=username,hospital=False)
        entry.save()

        user=User.objects.create_user(username=username,email=email,password=password,first_name=firstname,last_name=lastname)
        user.save()
        
        messages.info(request,'User created!!!')
        return render(request,'signup_government.html')



        # print(firstname," first name")
        # print(lastname," last name")
        # return render(request,'signup_government.html')
    else:
        return render(request,'signup_government.html')

    


@csrf_exempt
def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        obj=User.objects.filter(username=username)
        if not obj.exists():
            messages.info(request,"Register first!!")
            return redirect('signin')

        obj1=User.objects.get(username=username)
        # if obj1.password != password:
        #     messages.info(request,"Invalid credentials!!")
        #     return redirect('signin')

        # user1=auth.authenticate(username=username,password=password)
        # print("hello")

        # if user1 == None:
        #     messages.info(request,"Invalid credentials1!!")
        #     return redirect('signin')

        # auth.login(request,user1)

        # current_user=request.user
        
        # print(current_user.username," user name fetched from request")
        # print("logged in",request.user.username)
        # print(request.user,"request user1")
        # auth.logout(request)
        # print(request.user,"request user")

        # if request.user.is_authenticated:
        #     print("logged in",request.user.username)
        # else:
        #     print("logged out")






        return redirect('homehospital')
    else:
        return render(request,'signin.html')

@csrf_exempt
def homehospital(request):
    return render(request,'homehospital.html')

@csrf_exempt
def register(request):

    if request.method=='POST':
        user_name=request.POST['user_name']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        # user=User.objects.create_user(username=user_name,email=email,password=password,first_name=first_name,last_name=last_name)
        # user.save()
        test=User.objects.get(username=user_name)
        print(test.email)
        # return redirect('/')
        return render(request,'signin.html')



    else:
        return render(request,'register.html')
    

