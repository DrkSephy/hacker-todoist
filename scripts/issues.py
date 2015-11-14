# Grab all issues from a Github repo
import requests
import json

issues = requests.get('https://api.github.com/repos/legionJS/legionJS/issues?state=all')
data = json.loads(issues.text)

# Iterate over each dictionary
# data is an array of python dictionaries

# Store all the User data (will be posted to Todoist)
users = []

for datum in data:
		user = {}
		if datum['assignee'] != None:
				user['username'] = datum['assignee']['login']
				user['description'] = datum['body']
				user['due'] = datum['milestone']['due_on']
				users.append(user)

print users