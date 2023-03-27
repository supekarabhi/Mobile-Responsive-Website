from django.shortcuts import render

def home(request):
 return render(request, 'app/index.html')

def contact(request):
 return render(request, 'app/contact.html')

def about(request):
 return render(request, 'app/about.html')


def profile(request):
 return render(request, 'app/profile.html')

def biteergourd(request):
 return render(request, 'app/biteergourd.html')

def bringle(request):
 return render(request, 'app/bringle.html')

def brocoli(request):
 return render(request, 'app/brocoli.html')

def cabbage(request):
 return render(request, 'app/cabbage.html')

def chilli(request):
 return render(request, 'app/chilli.html')

def cucumber(request):
 return render(request, 'app/cucumber.html')

def flower(request):
 return render(request, 'app/flower.html')

def marigold(request):
 return render(request, 'app/marigold.html')

def sugarcane(request):
 return render(request, 'app/sugarcane.html')

def tomato(request):
 return render(request, 'app/tomato.html')

def watermelon(request):
 return render(request, 'app/watermelon.html')
