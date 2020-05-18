from accounts.models import Account
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def get_username_for_auth(input_username):
    # Account owner may want to signin with phone
    username = input_username
    if not input_username.__contains__("@"):
        # Check if a phone number exists
        if Account.objects.filter(phone=username).exists():
            account = Account.objects.get(phone=input_username)
            username = account.user.username
    else:
        if Account.objects.filter(email=input_username).exists():
            account = Account.objects.get(email=input_username)
            username = account.user.username
    return username


@login_required
def home(request):
    if is_staff(request.user):
        print("The user is a STAFF")
        return redirect('staff_profile')
    elif is_senior_staff(request.user):
        print("The user is a SENIOR STAFF")
        return redirect('senior_staff_profile')
    elif is_manager(request.user):
        print("The user is a MANAGER")
        return redirect('manager_profile')
    elif request.user.has_perm('user.is_superuser'):
        print("The user is a SUPERUSER STAFF")
        # logout(request)
        return redirect('profile')


def is_staff(user):
    if Account.objects.filter(user=user):
        account = Account.objects.get(user=user)
        # confirm that the user is a staff
        # if account.user_type == 0:
        if account.user_type == Account.STAFF:
            return True
        return False


def is_senior_staff(user):
    if Account.objects.filter(user=user):
        account = Account.objects.get(user=user)
        # confirm that the user is a staff
        if account.user_type == Account.SENIOR_STAFF:
            return True
        return False


def is_manager(user):
    if Account.objects.filter(user=user):
        account = Account.objects.get(user=user)
        # confirm that the user is a staff
        if account.user_type == Account.MANAGER:
            return True
        return False
