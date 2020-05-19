from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages

from accounts.utils import is_manager
from children.models import Child
from children.forms import ChildRegisterForm, ChildModifyForm


def register_child(request):
    if not is_manager(user=request.user):
        print("You are permitted")
        logout(request)
        return redirect('login')

    if request.method == 'POST':
        form = ChildRegisterForm(request.POST)
        if form.is_valid():
            # password = form.cleaned_data['password']
            # username = form.cleaned_data['email']
            # new_user =User.objects.create_user(username=username, email=username, password=password)
            # new_user.save()
            # account = form.save(commit=False)
            # account.user = new_user
            # account.email = username
            # account.save()
            form.save(commit=True)
            messages.success(request, "New child successfully registered")
            return redirect('children_list')
    else:
        form = ChildRegisterForm()
    return render(request, "children/register_child.html", {"form": form})


def children_list(request):
    children = Child.objects.all()
    context = {"children_list": children}
    return render(request, "children/children_list.html", context)


def modify_child_details(request, child_id=None):
    if not is_manager(user=request.user):
        print("You are permitted")
        logout(request)
        return redirect('login')

    child = get_object_or_404(Child, id=child_id)
    form = ChildModifyForm(request.POST or None, request.FILES or None, instance=child)
    if form.is_valid():
        updated = form.save()
        messages.success(request, "Child successfully updated")
        return redirect('children_list')
    context = {"child": child, "form": form}
    return render(request, "children/modify_child_details.html", context)
