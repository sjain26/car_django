from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib.auth.signals import user_login_failed
from django.dispatch import receiver


@receiver(user_logged_in, sender=User)
def Login_success(sender, request, user, **kwargs):
    print("...log_in...successfully.....")
    print("request----", request)
    print("sender :--", sender)
    print("user---", user)

    print("password", user.password)


@receiver(user_logged_out, sender=User)
def Log_out_success(sender, request, user, **kwargs):
    print(".......")
    print("____user log out successfully______")
    print("request----", request)
    print("sender :--", sender)
    print("user---", user)

    print("password", user.password)


@receiver(user_login_failed, sender=User)
def Login_failed(sender, credentials, request, **kwargs):

    print(".......")
    print("____user log failed______")
    print("request----", request)
    print("sender :--", sender)
    print("credentials---", credentials)
