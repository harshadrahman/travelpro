from django.http import HttpResponse
from django.shortcuts import render
from.models import place
from.models import destination

# Create your views here.
def demo(request):
    name="india"
    obj=place.objects.all()
    sal=destination.objects.all()
    return render(request,'index.html',{'result':obj,'sample':sal})
# def about(request):
#     return render(request,'about.html')
# def contact(request):
#     return HttpResponse('hello about contact')
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,'result.html',{'result':res})
