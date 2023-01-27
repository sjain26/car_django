from django.shortcuts import render
from django.core.mail import send_mail
from .models import CarList, Buyer
from django.views import View
from django.shortcuts import HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


# class CreateUserView(TemplateView):
#     template_name = 'signup.html'

#     def post(self, request):
#         if request.user.is_authenticated:
#             return redirect('home')
#         else:
#             uname = request.POST.get('username')
#             email = request.POST.get('email')
#             pass1 = request.POST.get('password1')
#             pass2 = request.POST.get('password2')
#             if pass1 != pass2:
#                 return HttpResponse(
#                     "Your password and confrom password are not Same!!")
#             else:
#                 my_user = User.objects.create_user(uname, email, pass1)
#                 my_user.save()
#                 return redirect('login')
        

class CarListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'home'
    model = CarList
    queryset = CarList.sellmanager.available()
    template_name = 'homepage.html'
    # context_object_name ='dataset'


class MyAdmin():   
    def get(request, id):
        print("my id=====", id)
        CarList.sellmanager.make_available(id)
        context = {}
        context['msg'] = "Successfully"
        return render(request, 'end.html', context)
   
   
@login_required(login_url='login')
def home_page(request):
    if request.user.is_authenticated:
        context = {}
        context['dataset'] = CarList.sellmanager.available()
        return render(request, 'homepage.html', context)


def sign_up_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            uname = request.POST.get('username')
            email = request.POST.get('email')
            pass1 = request.POST.get('password1')
            pass2 = request.POST.get('password2')
            if pass1 != pass2:
                return HttpResponse(
                    "Your password and confrom password are not Same!!")
            else:

                my_user = User.objects.create_user(uname, email, pass1)
                my_user.save()
                return redirect('login')
        return render(request, 'signup.html')


def login_page(request):
    print(request)
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            pass1 = request.POST.get('pass')
            user = authenticate(request, username=username, password=pass1)
            if user.is_superuser:
                context = {}
                context['dataset'] = CarList.sellmanager.selled_car()
                return render(request, 'myadmin.html', context)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse("Username or Password is incorrect!!!")
        return render(request, 'login.html')
        

def logout_page(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def buy_car(request, id):
    print("dffdj", id)
    context = {}
    context['dataset'] = CarList.sellmanager.available()
    request.session['ids'] = id
    return render(request, "consumer.html", context)


@login_required(login_url='login')
def sold_car(request):
    ids = request.session.get('ids')
    CarList.sellmanager.sold_car(ids)
    user = CarList.objects.filter(id=ids).values()
    modelname = user[0]['model_name']
    sellername = user[0]['seller_name']
    price = user[0]['asking_price']
    if request.method == 'POST':
        customer_name = request.POST['customer']
        mobile = request.POST['mobile']
        print("----------", customer_name, mobile)
        Buyer.objects.update_or_create(
            car_list_id=ids,
            buyer_name=customer_name,
            buyer_mobile=mobile)
        email_body = """"in car {0}  from {1} price have {2} 
        interested customer will be {3} and mobile no. {4} and
        commission on basis 5%""".format(
            modelname,
            sellername,
            price,
            customer_name,
            mobile)
        print(email_body)
        # send_mail(
        #     'Subject here',
        #      email_body,
        #     'd85715255f94c2',
        #     ['jainsatyam26@gmail.com'],
        #     fail_silently=False,)
        return render(request, "end.html", ({"msg": "Successfully"}))