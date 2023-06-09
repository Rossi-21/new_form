from django.shortcuts import render

def index(request):
    context = {
        'cities' : ['Seattle', 'New York', 'Chicago', 'San Fransisco'],
        'languages' : ['python', 'java', 'javascript', 'go', 'c#', 'c++']
    }
    return render(request, "index.html", context)

def create(request):
    name = request.POST['name']
    city = request.POST['city']
    language = request.POST['language']
    comments = request.POST['comments']

    context = {
    	"name" : name,
    	"language" : language,
        "city" : city,
        "comments" : comments
    }
    return render(request,"show.html", context)