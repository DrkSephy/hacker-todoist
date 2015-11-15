from scripts import issues
from django.shortcuts import render, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
	return HttpResponse('Hello!')

@csrf_exempt
def test(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		repo = request.POST.get('repo')
		service = request.POST.get('service')
		data = issues.batchTasks(username, repo, service)
		return HttpResponse(json.dumps(data));
		#return render(request, 'app/page.html', {'data': json.dumps(data)})
	else:
		print 'Not a post request?'
		return render(request, 'app/page.html')

@csrf_exempt
def events(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		dataToRemove = data['issue']['title']
		return render
	return HttpResponse('Demo events')