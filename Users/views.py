from django.shortcuts import render
from .forms import Login_Form

# Create your views here.
def about(request):
    if request.method=='POST':
        data=Login_Form(request.POST)
        if data.is_valid():
            data.save()
    return render(request, 'Users/about.html')