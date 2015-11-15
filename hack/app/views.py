from scripts import issues
from django.shortcuts import render, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from mongoengine import *
from models import Entries
connect('tumblelog')

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
		# Store in database
		for datum in data:
			print datum
			if 'due' in datum:
				entry = Entries(due=datum['due'], title=datum['title'], username=datum['username'])
				entry.save()
			else:
				entry = Entries(due='', title=datum['title'], username=datum['username'])
				entry.save()
		return HttpResponse(json.dumps(data));
	else:
		print 'Not a post request?'
		return render(request, 'app/page.html')

@csrf_exempt
def events(request):
	if request.method == 'POST':
		if request.body:
			data = json.loads(request.body)
			dataToRemove = data['issue']['title']
			newData = issues.batchTasks('DrkSephy', 'Shogi', 'github')
			for datum in newData:
				if datum['title'] == dataToRemove:
					newData.remove(datum)
			print newData	
	return HttpResponse('Demo events')

@csrf_exempt
def fetchDatabase(request):
	data = []
	for entry in Entries.objects:
		datum = {}
		datum['due'] = entry.due
		datum['title'] = entry.title
		datum['username'] = entry.username
		data.append(datum)
	print data
	return HttpResponse(json.dumps(data))