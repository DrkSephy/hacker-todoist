from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
	return HttpResponse('Hello!')

def test(request):
    return render(request, 'app/page.html')


