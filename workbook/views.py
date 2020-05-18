from django.shortcuts import render

from workbook.models import StaffTask, Task
from workbook.forms import StaffTaskForm
from accounts.utils import get_username_for_auth, is_manager



def create_task(request):
    if not is_manager(user=request.user):
        print("You are permitted")
        logout(request)
        return redirect('login')

    if request.method == 'POST':
        form = StaffTaskForm(request.POST)
        if form.is_valid():

            task = form.save(commit=False)
            task.save()
    else:
        form = StaffTaskForm()
    return render(request, "task/create_task.html", {"form": form})
