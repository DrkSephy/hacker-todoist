import requests
import moment
import json

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

