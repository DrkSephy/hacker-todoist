from scripts import issues
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
	return HttpResponse('Hello!')

def test(request):
	if request.method == 'POST':
		username = request.POST.get('user')
		repo = request.POST.get('repo')
		service = request.POST.get('service')
		data = issues.batchTasks(username, repo, service)
		return render(request, 'app/page.html', {'data': data})
	else:
		print 'Not a post request?'
		return render(request, 'app/page.html')


