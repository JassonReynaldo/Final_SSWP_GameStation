from django.shortcuts import render
from GameList.models.official_web import Official_Web

def index(request):
    if request.method == 'POST':
        search = request.POST.dict()
        name = search['name']
        official_webs = Official_Web.objects.filter(name__contains=name)
    else:
        official_webs = Official_Web.objects.all()  
    data = {
        'official_webs': official_webs,
    }

    return render(request, 'official_web/index.html', context=data)