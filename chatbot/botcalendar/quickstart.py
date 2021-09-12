from __future__ import print_function
import datetime
from datetime import datetime,timedelta
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import requests
import time
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

myId= '9fjf5s243jbb3kqic367v9883g@group.calendar.google.com'
def my_calendar():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('calendar', 'v3', credentials=creds)

def call_calendar(service):
    # Call the Calendar API
    now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId= myId, timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print (start, event['summary'])

    #verify events (in construction)
def verify_events(service):
    page_token = None
    while True:
        events = service.events().list(calendarId=myId).execute()
        for event in events['items']:
            print (event.get('summary'))
        page_token = events.get('nextPageToken')
        if event['summary'] == None:
            break    

    
    #creating event
def new_event(service):
        
    # Refer to the Python quickstart on how to setup the environment:
    # https://developers.google.com/calendar/quickstart/python
    # Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
    # stored credentials.
    new_event= input('gostaria de criar um evento novo?\n')
    if new_event == 'sim':
        sumary = input('qual o nome do evento?\n')
        location = input('onde vai ser?\n')
        dateM = input('qual data você quer marcar?\n')
        hourM = input('A que horas?\n')
        formatgeral = dateM+" "+hourM
        #transforming date and time in ISO 8601

        #initDate records start of event
        initDate =  datetime.strptime(formatgeral, "%d/%m/%y %H:%M").isoformat()
        timecal = datetime.strptime(formatgeral, "%d/%m/%y %H:%M") + timedelta(hours=1)
        timeTransform = datetime.strftime(timecal, "%d/%m/%y %H:%M")
        #finalDate records end of event
        finalDate = datetime.strptime(timeTransform, "%d/%m/%y %H:%M").isoformat()

        description = input('descreva algo sobre o evento:\n')
        emailp1=input('qual email vai participar?\n')
       
        event = {
        'summary': sumary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': initDate,
            'timeZone': 'America/Sao_Paulo',
        },
        'end': {
            'dateTime': finalDate,
            'timeZone': 'America/Sao_Paulo',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=1'
        ],
        'attendees': [
            {'email': emailp1},
            {'email': 'sbrin@example.com'},
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        },
        }

        event = service.events().insert(calendarId=myId, body=event).execute()
        #print ('Evento criado!: %s' % (event.get('htmlLink')))
        
        print('evento criado!') 
    else:
        print('tudo bem, fica pra próxima!')

def main():
    
    service = my_calendar() 
    verify_events(service)
   

if __name__ == '__main__':
    main()