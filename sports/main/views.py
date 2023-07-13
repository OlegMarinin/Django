from django.shortcuts import render
data = {'title':'Головна сторінка', 'values': ['sos', 'aaaa', 'vvvvv']}
def index(request) :
    return render(request, 'main/index.html', data)

def hadu(request):
    return render(request, 'main/hadu.html')

def contacts(request):
    return render(request, 'main/contacts.html')