from django.shortcuts import render, redirect

from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout
	)

from .forms import UserLoginForm, UserRegisterForm, PasswordResetForm
# for authetification mail
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
from django.core.mail import EmailMessage

from accounts.models import UserMoreFields
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from datetime import datetime

User = get_user_model()


def login_view(request):
	next = request.GET.get('next')
	form = UserLoginForm(request.POST or None)

	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')

		email_qs = User.objects.filter(email=username)
		if email_qs.exists():
			username =  User.objects.get(email=username).username

		CurrentUserID = User.objects.get(username=username).pk

		check_is_link_auth = UserMoreFields.objects.get(user_id=
			                                  CurrentUserID).is_link_auth
		if not check_is_link_auth:
			return HttpResponse('Please Activate your Account per email')

		user = authenticate(username=username, password=password)
		login(request, user)
		if next:
			return redirect(next)
		
		responseData = {
	        'id': 4,
	        'name': 'Test Response',
	        'roles' : ['Admin','User']
        }
		#return JsonResponse(responseData)
		return redirect('/')
	context = {
		'form': form,
	}
	return render(request, "login.html", context)


def register_view(request):
	next = request.GET.get('next')
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.is_active = True # TODO

		#name = form.cleaned_data.get('name')
		#surname = form.cleaned_data.get('surname')
		#phone = form.cleaned_data.get('phone')
		#is_link_auth = form.cleaned_data.get('is_link_auth')

		user.save()

		User = get_user_model()
		#Add phone + is_link_auth to database
		phone = form.cleaned_data.get('phone')
		is_link_auth = form.cleaned_data.get('is_link_auth')

		CurrentUserID = User.objects.get(username=
								form.cleaned_data.get('username')).pk

     	# Send an email to the user with the token:
		mail_subject = 'Activate your account.'
		current_site = get_current_site(request)
		activation_url_pattern = 'accounts/activate'
		uid = urlsafe_base64_encode(force_bytes(user.pk))
		token = account_activation_token.make_token(user)
		activation_link = "{0}/{1}/?uid={2}&token{3}".format(current_site,
														 activation_url_pattern,
			                                             uid, token)
		message = "Hello {0},\n {1}".format(user.username, activation_link)
		to_email = form.cleaned_data.get('email')
		email = EmailMessage(mail_subject, message, to=[to_email])
		email.send()
		
		# current date and time + UserMoreFields save
		now = datetime.now()
		timestamp_now = datetime.timestamp(now)

		timestamp_expire = timestamp_now + 86500 # = more then one day

		UserMre = UserMoreFields(phone=phone,
			                    is_link_auth=is_link_auth,
			                    token=token,
			                    timestampNow=timestamp_now,
			                    timestampExp=timestamp_expire,
			                    user_id=CurrentUserID)
		UserMre.save()
		#if (timestampNew - timestamp) >= 86400: # one day in secconds
		#    print("too late mate")
		#    print((timestampNew - timestamp))
		return HttpResponse('Please confirm your email address to complete the registration')

		login(request, new_user)
		if next:
			return redirect(next)
		return redirect('/')

	context = {
		'form': form,
	}
	return render(request, "signup.html", context)

def logout_view(request):
	logout(request)
	return redirect('/')

# for authehtification mails
def ActivateAccount_view(request):
    request_string = str(request)
    Positiontoken = request_string.find('token')
    Positiontoken_Last = len(request_string)
    # +5 fuer "token" & -2 fuer "\n + ' "
    token_from_string = request_string[(Positiontoken+5):(Positiontoken_Last-2)]

    field_object = UserMoreFields._meta.get_field('token')
    obj = UserMoreFields.objects.filter(token=token_from_string)
    if not obj.exists():
       return HttpResponse('Activation link is invalid!')

    obj_list = list(obj);
    current_user_id = obj_list[0].user_id
    obj.filter(user_id=current_user_id).update(is_link_auth=True)

    return HttpResponse('Account activated')

