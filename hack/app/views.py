from scripts import issues
from django.shortcuts import render, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from mongoengine import *
from models import Entries, BitbucketEntries, Notifications
from twilio.rest import TwilioRestClient 

account_sid = "AC7889a1889c1833bd7181e45e60372776"
auth_token = "ff941c0db497765c7852909086c77ef1"
client = TwilioRestClient(account_sid, auth_token) 

connect('tumblelog')

# Create your views here.

def index(request):
	return HttpResponse('Hello!')

@csrf_exempt
def test(request):
	if request.method == 'POST':
		if request.POST.get('twilioNumber'):
			twilioUser = request.POST.get('twilioNumber')
			print twilioUser
			number = Notifications(number=str(twilioUser))
			number.save()
			return render(request, 'app/page.html')
		else: 
			username = request.POST.get('username')
			repo = request.POST.get('repo')
			service = request.POST.get('service')
			data = issues.batchTasks(username, repo, service)
			
			client.messages.create(
			    to="+13473282978", 
			    from_="+13473259195", 
			    body="David, you have to present at Hack battle soon!", 
			)
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
			if service == 'bitbucket':
				for datum in data:
					entry = BitbucketEntries(due='', title=datum['title'], username=datum['username'])
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

@csrf_exempt
def fetchBitbucketDatabase(request):
	data = []
	for entry in BitbucketEntries.objects:
		datum = {}
		datum['due'] = entry.due
		datum['title'] = entry.title
		datum['username'] = entry.username
		data.append(datum)
	return HttpResponse(json.dumps(data))

@csrf_exempt
def clearDatabases(request):
	for entry in Entries.objects:
		entry.delete()
	for entry in BitbucketEntries.objects:
		entry.delete()
	for entry in Notifications.objects:
		entry.delete()
	return HttpResponse('Cleared the database!')

@csrf_exempt
def fetchNumbers(request):
	data = []
	for entry in Notifications.objects:
		datum = {}
		datum['number'] = entry.number
		data.append(datum)
	return HttpResponse(json.dumps(data))