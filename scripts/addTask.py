from pytodoist import todoist
import secrets

user = todoist.login(secrets.credentials['username'], secrets.credentials['password'])
project = user.get_project('Github')
project.add_task('New Task!')

