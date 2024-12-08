from django.shortcuts import render


def base(request):
    return render(request, 'pro/base.html')


def about(request):
    return render(request, 'pro/about.html')


def services(request):
    return render(request, 'pro/services.html')


def contact(request):
    return render(request, 'pro/contact.html')


def login(request):
    return render(request, 'pro/login.html')


def reg(request):
    return render(request, 'pro/reg.html')


def appointment(request):
    return render(request, 'pro/appointment.html')


def profile(request):
    return render(request, 'pro/profile.html')


def edit(request):
    return render(request, 'pro/edit.html')


def settings(request):
    return render(request, 'pro/settings.html')


def logout(request):
    return render(request, 'pro/logout.html')


def dashboard(request):
    return render(request, 'pro/dashboard.html')


def catalog(request):
    return render(request, 'pro/catalog.html')


def learn(request):
    return render(request, 'pro/learn.html')


def pharmacy(request):
    return render(request, 'pro/pharmacy.html')
