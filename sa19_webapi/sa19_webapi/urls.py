from django.contrib import admin
from django.urls import path, include

from .views import home
from accounts.views import login_view, register_view, logout_view, ActivateAccount_view


#von dude
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
#

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', home),
    path('accounts/login/', login_view),
    path('accounts/register/', register_view),
    path('accounts/logout/', logout_view),
    path('accounts/activate/', ActivateAccount_view),


    # for passwor resetting
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    #path('', include('blog.urls')),


    # 1 path fuer authentification
]
