import code
from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import redirect
from .models import urls
import string    
import random
# Create your views here.
def index (request) :
    if request.method == "POST":
       # getting input with name = fname in HTML form
       uls = request.POST['uls']
       urlv=urls.objects.all()
       if(urls.objects.filter(website=uls).exists()):
                ran=urls.objects.get(website=uls)
                print(uls,ran.code)
                ulr="127.0.0.1:8000/"+ran.code
       else:
                ran = ''.join(random.choices(string.ascii_lowercase , k = 5))
                print(uls,ran)
                b = urls(website=uls, code=ran)
                b.save()
                ulr="127.0.0.1:8000/"+ran
       params={'rans' : ulr}
       return render(request,'index1.html',params)
    
    else :
        params={'rans': 0 }
        return render(request,'index1.html',params)    

def urlRedirect(request, slugs):
    data = urls.objects.get(code = slugs)
    return redirect('http://'+data.website)
