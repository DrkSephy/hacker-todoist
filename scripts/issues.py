# Grab all issues from a Github repo
import requests
import json

issues = requests.get('https://api.github.com/repos/legionJS/legionJS/issues?state=all')
data = json.loads(issues.text)


