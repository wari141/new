from django.shortcuts import render

from my_app.models import customer


# Create your views here.
def home(request):
    if request.method == 'POST':
        names = request.POST['name']
        emails = request.POST['email']
        phones = request.POST['phone']
        passwords = request.POST['password']
        weight = request.POST['weight']
        gender = request.POST['gender']
        height = request.POST['height']
        customer.objects.create(name=names, email=emails, phone=phones, password=passwords, weight=weight, gender=gender, height=height)
        count =customer.objects.all().count()
        print(f"{count} customers ")
    return render(request, 'home.html')