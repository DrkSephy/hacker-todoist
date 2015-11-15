# Grab all issues from a Github repo
import requests
import json
import moment
import bitbucket


def batchBitbucketTasks(username, repository):
	issues = requests.get('https://bitbucket.org/api/1.0/repositories' + '/' + username + '/' + repository + '/issues')
	data = json.loads(issues.text)
	users = []

	for datum in data['issues']:
		user = {}
		if datum['responsible']['username'] == 'DrkSephy':
			user['username'] = datum['responsible']['username']
			user['title'] = datum['title']
			user['priority'] = datum['metadata']['kind']
			users.append(user)	
	return users


def batchTasks(username, repository, service):
	"""
	Fetches all issues for the given user in a repository from
	the specified service
	"""
	if service == 'github':
		issues = requests.get('https://api.github.com/repos/' + username + '/' + repository + '/issues?state=all&client_id=f4c46f537e5abec0d5b0&client_secret=53ba628c38e4f8adca7d467573a13989b4546743')
		data = json.loads(issues.text)

		# Store all the User data (will be posted to Todoist)
		users = []

		for datum in data:
				user = {}
				if datum['assignee'] != None:
						if datum['assignee']['login'] == 'DrkSephy':
							user['username'] = datum['assignee']['login']
							user['title'] = datum['title']
							m = moment.date(datum['milestone']['due_on'], '%Y-%m-%dT%H:%M:%SZ')
							user['due'] = m.format('YYYY-M-D H:M')
							users.append(user)
		return users
	else:
		data = batchBitbucketTasks(username, repository)
		return data

	

