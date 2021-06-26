from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import user_details
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from .models import EmailConfirmed, add_contest
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    all_contest = add_contest.objects.all()
    all_contest_count = add_contest.objects.all().count()
    context = {'all_contest':all_contest, 'all_contest_count':all_contest_count}
    return render(request, 'index.html', context)

def login_function(request):
    if request.method == 'POST':
        log_username = request.POST['email']
        log_password = request.POST['password']
        # this is for authenticate username and password for login
        user = authenticate(username=log_username, password=log_password)

        erorr_message_2 = ""

        if user is not None:
            login(request, user)
            # messages.success(request, "Successfully Logged In !!")
            return redirect('index')
        else:
            erorr_message_2 ="Invalid Credentials, Please Try Again !!"

            value_func2 = {'erorr_message_2': erorr_message_2, 'log_username': log_username}
            # messages.error(request, "Invalid Credentials, Please Try Again !!")
            return render(request, 'loginPage.html', value_func2)
    else:

        return render(request, 'loginPage.html')

def register(request):
    if request.method == 'POST':
        # check the post peramiters
        sign_first_name = request.POST['firstname']
        sign_last_name = request.POST['lastname']

        phone = request.POST['phone']
        sign_username = request.POST['email']
        sign_email = request.POST['email']
        sign_password = request.POST['password']
        confirm_sign_password = request.POST['password_confirm']


        # chech the error inputs

        user_username_info = User.objects.filter(username=sign_username)
        user_email_info = User.objects.filter(email=sign_email)

        # if user_username_info:
        #     messages.error(request, "Username Already Exist")
        #     return redirect('register')
        #
        # if user_email_info:
        #     messages.error(request, "Email Already Exist")
        #     return redirect('register')
        #
        # if sign_password != confirm_sign_password:
        #     messages.error(request, "Passwords are not matching !")
        #     return redirect('register')
        #
        # if len(sign_password) < 7:
        #     messages.error(request, "Passwords Must be Al least 7 Digits")
        #     return redirect('register')

        erorr_message = ""

        if user_username_info:
            # messages.error(request, "Username Already Exist")
            erorr_message = "Email Already Exist"

        elif user_email_info:
            # messages.error(request, "Email Already Exist")
            erorr_message = "Email Already Exist"

        elif sign_password != confirm_sign_password:
            # messages.error(request, "Passwords are not match")
            erorr_message = "Passwords are not match"

        elif len(sign_password) < 7:
            # messages.error(request, "Passwords Must be Al least 7 Digits")
            erorr_message = "Passwords Must be Al least 7 Digits"

        if not erorr_message:

            # create user
            myuser = User.objects.create_user(sign_username, sign_email, sign_password)
            myuser.first_name = sign_first_name
            myuser.last_name = sign_last_name
            myuser.is_active = False
            myuser.save()

            user_details_more = user_details(user=myuser, Phone_No=phone)
            user_details_more.save()

            # send mail
            user = EmailConfirmed.objects.get(user=myuser)
            site = get_current_site(request)
            email = myuser.email
            first_name = myuser.first_name
            last_name = myuser.last_name

            sub_of_email = "Activation Email From Tombitrip."
            email_body = render_to_string(
                'verify_email.html',
                {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'domain': site.domain,
                    'activation_key': user.activation_key
                }
            )

            send_mail(
                sub_of_email,  # Subject of message
                email_body,  # Message
                '',  # From Email
                [email],  # To Email

                fail_silently=True
            )

            messages.success(request, 'Check Your Email for Activate Your Account !!!')

            return redirect('/')

        else:

            value_dic = {'sign_email': sign_email, 'sign_first_name': sign_first_name,
                         'sign_last_name': sign_last_name, 'phone':phone, 'erorr_message':erorr_message}
            return render(request, 'signupPage.html', value_dic)

    return render(request, 'signupPage.html')




def func_logout(request):
    # this is for logout from user id
    logout(request)
    return redirect('index')


def email_confirm(request, activation_key):
    user= get_object_or_404(EmailConfirmed, activation_key=activation_key)
    if user is not None:
        user.email_confirmed=True
        user.save()

        myuser=User.objects.get(email=user)
        myuser.is_active=True
        myuser.save()

        activated_user_f_name=myuser.first_name
        activated_user_l_name=myuser.last_name
        context = {'activated_user_f_name':activated_user_f_name, 'activated_user_l_name':activated_user_l_name}

        return render(request, 'registration_complete.html', context)



def profile(request):
    user = request.user
    get_user_phone = user_details.objects.get(user=user)
    context1 = {'get_user_phone':get_user_phone}
    return render(request, 'profile.html', context1)


def mycontest(request):

    context1 = {}
    return render(request, 'mycontest.html', context1)


def myearnings(request):

    context1 = {}
    return render(request, 'myearnings.html', context1)


def myresults(request):

    context1 = {}
    return render(request, 'myresults.html', context1)

