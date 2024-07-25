import datetime
import random

from django.shortcuts import render

# Create your views here.
def result_view(request):
    msg_list = [
        'The golden days are  ahead',
        'Better to sleep more in the class',
        'Tomorrow will be the best day of your life',
        'Tomorrow is the perfect day to propose ur gf',
        'Very soon you will get job',
    ]
    name_list = ['Sunny','Mallika','Katrina','Kareena','Deepika','Samantha']
    date = datetime.datetime.now()
    h = int(date.strftime('%H'))
    if h <=12:
        s = 'Good Morning'
    elif h < 16:
        s = 'Good afternoon'
    elif h <21:
        s = 'Good Evening'
    else:
        s = 'Good Night'
    name = random.choice(name_list)
    msg =random.choice(msg_list)
    my_dict = {'date':date,'name':name,'msg':msg,'wish':s}
    return render(request,'testapp/astrology.html',my_dict)