# awake.api
# Module for handling APIs

import requests

ROOT_URL = 'https://agile-spire-43204.herokuapp.com'
AUTH_URL = ROOT_URL+'/api/authenticate'
USERS_URL = ROOT_URL+'/api/users'
TODAY_URL = ROOT_URL+'/api/today'
AWAKEN_URL = ROOT_URL+'/api/awakenings'

def register(username, password):
   '''Register an acount with given credentials
      True: Successful registration
      False: Failed registration - Username already taken
      None: Something went wrong
   '''
   r = requests.post(USERS_URL, json={
         'user': {
            'username': username,
            'password': password,
            'password_confirmation': password
         }
      })
   if r.status_code == 201:
      return True
   elif r.status_code == 422:
      return False
   else:
      return None

def login(username, password):
   '''Login with given credentials to obtain JWT
      'eyJ0eXAiOiJKV...': Successful login
      '': Failed login - Wrong username and/or password
      None: Something went wrong
   '''
   r = requests.post(AUTH_URL, json={
         'auth': {
            'username': username,
            'password': password
         }
      })
   if r.status_code == 200:
      return r.json()['jwt']
   elif r.status_code == 404:
      return ''
   else:
      return None

def today():
   '''Get list of all users with today's awakening time
      [('chunkhang', '07:30 am'), ()...]: List of today
      None: Something went wrong
   '''
   r = requests.get(TODAY_URL)
   if r.status_code == 200:
      today_list = []
      for user in r.json()['users']:
         today_list.append((user['username'], user['awaken_time']))
      return today_list
   else:
      return None

def awaken(token):
   '''Record awakening time
      True: Successfully recorded
      None: Something went wrong
   '''
   r = requests.post(AWAKEN_URL, headers={
         'Authorization': token
      })
   if r.status_code == 201:
      return True
   else:
      return None