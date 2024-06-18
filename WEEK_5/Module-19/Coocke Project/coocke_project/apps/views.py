from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta

# cookie---
def home(request):
    response = render(request, './home.html')
    response.set_cookie('name', 'rahim')
    # response.set_cookie('name', 'karim', max_age=6)
    response.set_cookie('name', 'karim', expires=datetime.utcnow()+timedelta(days=7))
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, './get_cookie.html', {'name' : name})    


def delete_cookie(request):
    response = render(request, './del.html')
    response.delete_cookie('name')
    return response

#Django Section---
def set_section(request):
    data = {
        'name' : 'rahim',
        'age' : 23,
        'language' : 'bangla'
    }    
    print(request.session.get_session_cookie_age())
    print(request.session.get_expiry_date()) 
    request.session.update(data)
    return render(request,'home.html')

def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name', 'Guest')
        request.session.modified = True
        # age = request.session.get('age')
        return render(request, 'get_session.html', {'name' : name})#age' : age 
    else:
        return HttpResponse("Your Section Has Been Expired. Login Again")

def delete_session(request):
    # del request.session['name']
    request.session.flush()
    # request.session.clear_expired()
    return render(request, 'del.html')