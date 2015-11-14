# Grab all issues from a Github repo
import requests
import json

# Iterate over each dictionary
# data is an array of python dictionaries

def batchTasks(username, repository):
	"""
	Fetches all Github issues for the given user in a repository.
	"""

	issues = requests.get('https://api.github.com/repos/' + username + '/' + repository + '/issues?state=all&client_id=f4c46f537e5abec0d5b0&client_secret=53ba628c38e4f8adca7d467573a13989b4546743')
	print 'https://api.github.com/repos/' + username + '/' + repository + '/issues?state=all&client_id=f4c46f537e5abec0d5b0&client_secret=53ba628c38e4f8adca7d467573a13989b4546743'
	data = json.loads(issues.text)

	# Store all the User data (will be posted to Todoist)
	users = []

	for datum in data:
			user = {}
			if datum['assignee'] != None:
					if datum['assignee']['login'] == 'DrkSephy':
						user['username'] = datum['assignee']['login']
						user['title'] = datum['title']
						user['due'] = datum['milestone']['due_on']
						users.append(user)
	return users


