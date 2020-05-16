from accounts.models import Account


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
