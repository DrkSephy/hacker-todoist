from trello import TrelloApi
import json

trello = TrelloApi('26971760681466f902c20d5a814b38f3')
print json.loads(trello.boards.get('4d5ea62fd76aa1136000000c'))

#trello.get_token_url('My App', expires='30days', write_access=True)
 #   'https://trello.com/1/authorize?key=TRELLO_APP_KEY&name=My+App&expiration=30days&response_type=token&scope=read,write'