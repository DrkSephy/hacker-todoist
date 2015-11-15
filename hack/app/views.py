from scripts import issues
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
	return HttpResponse('Hello!')

def test(request):
	data = issues.batchTasks('legionJS', 'legionJS')
	print data
	return render(request, 'app/page.html', {'data': data})


