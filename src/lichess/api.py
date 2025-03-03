import json

import requests

from tokens import TOKEN

BASE_URL = "https://lichess.org/"
headers = {
  "Authorization": "Bearer " + TOKEN,
  "Content-Type": "application/json",
}

'''
Documentation related to lichess bot APIs 
https://lichess.org/api#tag/Bot
'''
def get_account_info():
  url = BASE_URL + "api/account"
  return requests.get(url, headers=headers)

def get_online_bots():
  url = BASE_URL + "api/bot/online"
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
    bots = [json.loads(line) for line in response.text.splitlines()]
    return bots
  
  print('Error getting online bots,', response.status_code)
  return '[{}]'