from scripts import issues
from django.shortcuts import render, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from mongoengine import *
from models import Entries, BitbucketEntries
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
		if service == 'github':
			for datum in data:
				print datum
				if 'due' in datum:
					entry = Entries(due=datum['due'], title=datum['title'], username=datum['username'])
					entry.save()
				else:
					entry = Entries(due='', title=datum['title'], username=datum['username'])
					entry.save()
		else:
			for datum in data:
				print datum
				if 'due' in datum:
					entry = BitbucketEntries(due=datum['due'], title=datum['title'], username=datum['username'])
					entry.save()
				else:
					entry = BitbucketEntries(due=datum['due'], title=datum['title'], username=datum['username'])
					entry.save()
		return HttpResponse(json.dumps(data));
	else:
		print 'Not a post request?'
		return render(request, 'app/page.html')

@csrf_exempt
def events(request):
	if request.method == 'POST':
		if request.body:
			allEntries = []
			data = json.loads(request.body)
			dataToRemove = data['issue']['title']
			# Need to remove entry from database
			for entry in Entries.objects:
				datum = {}
				if entry.title == dataToRemove:
					print 'Removing entry'
					entry.delete()
				else:
					datum['due'] = entry.due
					datum['title'] = entry.title
					datum['username'] = entry.username
					allEntries.append(datum)
		print allEntries
	return HttpResponse(json.dumps(allEntries))

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