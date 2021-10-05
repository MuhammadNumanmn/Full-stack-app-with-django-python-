from django.shortcuts import render, HttpResponse

rooms = [
    {'id': 1, 'name': 'Lets learn Python'},
    {'id': 2, 'name': 'Lets learn Django'},
    {'id': 3, 'name': 'Lets learn React'},
    {'id': 4, 'name': 'Lets learn Cloud Computing'},

]

def Home(request):
    return render(request, 'home.html')