import requests
import moment
import json

req = requests.get('https://bitbucket.org/api/1.0/repositories/DrkSephy/test/issues')
data = json.loads(req.text)

users = []

for datum in data['issues']:
	user = {}
	if datum['responsible']['username'] == 'DrkSephy':
		user['username'] = datum['responsible']['username']
		user['title'] = datum['title']
		user['priority'] = datum['metadata']['kind']
		users.append(user)


