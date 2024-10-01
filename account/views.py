from .forms import CustomLoginForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


def custom_login(request):
    if request.method == "POST":
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
        return redirect("")
    else:
        form = CustomLoginForm()

    return render(request, "account/login.html", {"form": form})
