from django.shortcuts import render, redirect
from django.views import generic, View
from django.utils import timezone
import pyotp
from .models import Person, GasRequest
from .email import emailSend
import datetime
from .utils import reqid 

class Customer(generic.TemplateView):
    template_name = "customer/index.html"

    def post(self, request, *args, **kwargs):

        inputEmail = request.POST.get("email")
        print(inputEmail)

        user_exists = Person.objects.filter(email=inputEmail).exists()
        # print(datetime.datetime.now())
        otp_secret = pyotp.random_base32(32)
        print({"otp secret": otp_secret})
        request.session["token"] = otp_secret
        otp = pyotp.TOTP(otp_secret)
        print({"otp": otp})
        otp_code = otp.now()
        print({"otp Code": otp_code})
        request.session["email"] = inputEmail
        print(request.session["email"])

        if user_exists == True:
            Person.objects.filter(email=inputEmail).update(
                updated_at=datetime.datetime.now(), otp_secret=otp_secret
            )
            # emailSend(inputemail=inputEmail, otp= otp_code)

            return redirect("/verification/")
        elif user_exists == False:
            user = Person.objects.create(email=inputEmail, otp_secret=otp_secret)
            user.save()
            return redirect("/verification/")

        return render(request, "customer/index.html")


class Verification(generic.TemplateView):
    template_name = "customer/verification.html"

    def post(self, request):
        otp1 = request.POST.get("otp-1")
        otp2 = request.POST.get("otp-2")
        otp3 = request.POST.get("otp-3")
        otp4 = request.POST.get("otp-4")
        otp5 = request.POST.get("otp-5")
        otp6 = request.POST.get("otp-6")
        otp_code = f"{otp1}{otp2}{otp3}{otp4}{otp5}{otp6}"
        print(otp_code)
        email = request.session.get("email")
        request.session["otp"] = otp_code
        print(request.session["otp"])

        print({"verification": email})
        user_ex = Person.objects.filter(email=email).exists()
        if user_ex == True:
            user = Person.objects.get(email=email)
            otp = pyotp.TOTP(user.otp_secret)

            print(user.otp_secret)
            print(otp.verify(otp_code))

            if otp.verify(otp_code):
                if user.is_verified == True:
                    user.save()
                    return redirect("/profile/")
                if user.is_verified == False:
                    user.is_verified = True
                    user.save()
                    return redirect("/profile/")
            else:
                return redirect("/")


class Profile(View):

    def get(self, request):
        token = request.session["token"]
        print(token)
        email = request.session["email"]
        print(email)
        if email:
            user = Person.objects.get(email=email)
            print({"user email is": user.email})
            if token == user.otp_secret:
                return render(request, "customer/profile.html")
        else:
            return redirect("/")

    def post(self, request):
        data = request.POST
        email = request.session["email"]
        token = request.session["token"]
        print(token)
        print(data.get("address"))
        
        # print(user.pk)

        if data:
            try:
                if request.method == 'POST':
                    request.session['user_first_name'] = request.POST.get('first')
                    request.session['user_last_name'] = request.POST.get('last')
                    request.session['user_address'] = request.POST.get('address')
                    request.session['user_phoneNumber'] = request.POST.get('phoneNumber')
                    
                    # Now you can use these variables as strings
                    # print(request.session['user'])
                   
                    
                # print(request.POST)
                # request.session['user'] = request.POST.getlist('first')
                # print(request.POST.getlist('first')[1])
                # print(request.session['user'])
            except (ValueError):
               print(ValueError)
               
            return redirect("/customer/")


class Dashboard(View):

    def get(self, request):
        token = request.session["token"]
        print(token)
        email = request.session["email"]
        print(email)
        if email:
            user = Person.objects.get(email=email)
            print(user.id)
            if token == user.otp_secret:
                context = {
                'first_name': request.session.get('user_first_name'),
                "last_name" :request.session.get("user_last_name"),
                "email" :request.session.get("email"),
                "address" : request.session.get("user_address"),
                "phoneNumber" : request.session.get("user_phoneNumber"),
                }
                
                Gas_Req = {'request': GasRequest.objects.all().filter(email=email)}
                for i in Gas_Req:
                    print(i)
                OneContext = {**context, **Gas_Req}
                return render(request, "customer/dashboard.html", context=OneContext)
        else:  
            return redirect("/")

    def post(self, request):
        # print(request.POST.get("action"))
        data = request.POST
        print(data.get("action", "title"))
        if request.POST.get("action") == "Logout":
            del request.session["email"]
            del request.session["token"]
            # print(request.session['email'], request.session['token'])
            return redirect("/")
        elif data.get("title"):
            reqidNew = reqid()
            imageReq = request.FILES.get('imageReq')
            print(imageReq) 
            NewRequest = GasRequest.objects.create(
                first_name=data.get("first_name"),
                last_name=data.get("last_name"),
                title=data.get("title"),
                req_id = reqidNew,
                email=request.session["email"],
                discription=data.get("discription"),
                image = imageReq,
                submit_at=timezone.now(),
            )
            NewRequest.save()
            print(NewRequest)
            return redirect("/customer/")
        elif data.get("action") == "update":
            pass
        else:
            return render(request, "customer/dashboard.html")
        # elif request.POST.get("action") == "delete":
        #     view = QuestionDeleteView.as_view()
        #     return view(request, )


def Requests(request):
    return render(request, "customer/request.html")
