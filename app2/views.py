from django.shortcuts import render

# Create your views here.
def second(request):
    d={'favfood':'Biryani is my fav food'}
    return render(request,'second.html',context=d)

def third(request):
    d={'place':'Banglore climate is so cool'}
    return render(request,'third.html',d)
