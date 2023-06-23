from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import math
# Create your views here.

def test_app(request):
    template = loader.get_template('home.html')
    return render(request, 'home.html')


def test_app2(request):
   if request.method == 'POST':
       input_val = request.POST.get('input')
       
       lcm = 1
       for i in range(1,int(input_val)+1):
           lcm = int((lcm * i) / math.gcd(lcm, i))

       if int(input_val) > 0:   
            context = {
                 'answer': lcm,
             }
       else:
            context = {
                 'answer': 'Error you cannot work with a negative numbers or a zero',
             }
       return render(request, 'answer.html', context)