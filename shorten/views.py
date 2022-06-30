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
       ran = ''.join(random.choices(string.ascii_lowercase , k = 5))
       print(uls,ran)
       b = urls(website=uls, code=ran)
       b.save()
       ulr='127.0.0.1:8000/'+ran
       params={'rans' : ulr}
       return render(request,'index.html',params)
    
    else:
        return render(request,'index.html')    

def urlRedirect(request, slugs):
    data = urls.objects.get(code = slugs)
    return redirect('http://'+data.website)