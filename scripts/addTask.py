import secrets
import issues
from pytodoist import todoist

def sync(name):
	"""
	Creates a new project on todoist, and adds all Github
	issues into the todoist project.
	"""
	user = todoist.login(secrets.credentials['username'], secrets.credentials['password'])
	# name will be passed from a POST request
	# Create a project with name passed in
	user.add_project(name)
	# Get a hold of the project just created
	project = user.get_project(name)
	# Get issue data
	data = issues.batchTasks('legionJS', 'legionJS')
	for task in data:
		project.add_task(task['title'], date=task['due'])
	return

sync('Newest List')









