from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from accounts.models import UserMoreFields
from django.db import models
from django.contrib.auth.models import User

User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		#print("Bin hier")
		#CurrentUserEmail = User.objects.get(username=username).email
		#print("Hier kommt email: ", CurrentUserEmail)

		#ivebackuser = User.objects.get(email=username).username
		#print("Hier kommt user: ", ivebackuser)
		#try:
		#	givebackuser = User.objects.get(email=username).username
		#	print("Hier kommt user: ", givebackuser)
		#except:
		#	print("Either used Username or couldnt find email")

		if username and password:
			email_qs = User.objects.filter(email=username)
			if email_qs.exists():
				 username =  User.objects.get(email=username).username

			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError('This user does not exist')
			if not user.check_password(password):
				raise forms.ValidationError('Incorrect password')
			if not user.is_active:
				raise forms.ValidationError('This user is not active')
		return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
	#username = forms.CharField(label='Username')
	email = forms.EmailField(label='Email Address')
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)
	first_name = forms.CharField()
	last_name = forms.CharField()
	phone = forms.IntegerField()
	is_link_auth = forms.BooleanField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'password',
			'password2',
			'first_name',
			'last_name',
			'phone',
			'is_link_auth'
		]


	def clean(self, *args, **kwargs):
		#Add phone + is_link_auth to database
		#phone = self.cleaned_data.get('phone')
		#is_link_auth = self.cleaned_data.get('is_link_auth')
		#user_id = 23
		#UserMre = UserMoreFields(phone=phone, is_link_auth=is_link_auth, user_id=user_id)
		#UserMre.save()

		#Check Email
		email = self.cleaned_data.get('email')
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("This email is already being used")
		return super(UserRegisterForm, self).clean(*args, **kwargs)

class PasswordResetForm(forms.Form):
	email = forms.CharField()



	def clean(self, *args, **kwargs):
		email = self.cleaned_data.get('email')
		email_qs = User.objects.filter(email=email)
		if not email_qs.exists():
			raise forms.ValidationError("This email does not exists")
		return super(PasswordResetForm, self).clean(*args, **kwargs)

# for authentification
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token

User = get_user_model()

# class Activate(forms.Form):
#     def get(self, request, uidb64, token):
#         try:
#             uid = force_text(urlsafe_base64_decode(uidb64))
#             user = User.objects.get(pk=uid)
#         except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#             user = None
#         if user is not None and account_activation_token.check_token(user, token):
#             # activate user and login:
#             user.is_active = True
#             user.save()
#             login(request, user)
#
#             return render(request, 'activation.html', {'form': form})
#
#         else:
#             return HttpResponse('Activation link is invalid!')
