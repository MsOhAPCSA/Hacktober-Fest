from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        "title": "Hacktober-Fest",
    }
    return render(request,'index.html',context)