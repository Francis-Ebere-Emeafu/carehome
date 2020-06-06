from accounts.models import Account


def account(request):
    if request.user.is_authenticated:
        account = Account.objects.get(user=request.user)
        return {"account": account}
    else:
        return {"account": None}
