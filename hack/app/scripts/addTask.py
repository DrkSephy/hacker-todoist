import secrets
import issues
import bitbucket
from pytodoist import todoist

def sync(name, service):
	"""
	Creates a new project on todoist, and adds all <service>
	issues into the todoist project.
	"""
	user = todoist.login(secrets.credentials['username'], secrets.credentials['password'])
	# name will be passed from a POST request
	# Create a project with name passed in
	user.add_project(name)
	# Get a hold of the project just created
	project = user.get_project(name)
	# Get issue data
	if service == 'Github':
		data = issues.batchTasks('legionJS', 'legionJS')
		for task in data:
			project.add_task(task['title'], date=task['due'])
		return
	else:
		data = bitbucket.batchBitbucketTasks('DrkSephy', 'test')
		for task in data:
			print task['priority']
			project.add_task(task['title'])

sync('Github List', 'Github')









