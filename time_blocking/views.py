from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

# def login(request):
#     return HttpResponse("Hello User!")

# def register(request):
#     return render(request, "register.html")