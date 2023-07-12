from django.shortcuts import render


def Contact_Us(request):
    return render(request, 'contact_us.html')
