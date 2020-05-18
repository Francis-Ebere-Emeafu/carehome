from Home.models import Farmer, Buyer


def is_farmer(user):
    if Farmer.objects.filter(user=user):
        farmer = Farmer.objects.get(user=user)
        # confirm that the user is a farmer
        if farmer:
            return True
        return False


def is_buyer(user):
    if Buyer.objects.filter(user=user):
        buyer = Buyer.objects.get(user=user)
        # confirm that the user is a farmer
        if buyer:
            return True
        return False
