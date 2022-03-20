# Phase 1: IN PROGRESS
# Read, sort, & categorize alert mails.
# Ensure Outlook and monday.com inboxes remain in sync (firstly, just alerts)

# Phase 2: TBD
# Assign and categorize requests within outlook & monday.com
# Again, Ensuring outlook and monday.com remain in sync
# Ensure assignees are aware of their new jobs!

# Phase 3: TBD
# Develop solution to help speed up the process of inbox items that rely on manual inputs.
# (Templates/Generated Emails with confirmations?)
# Terminal based interface
# Rollback operations function???


import win32com.client
import json
import requests
from monday import MondayClient

outlook = win32com.client.Dispatch("outlook.application").GetNamespace("MAPI")
mailbox = outlook.Folders.Item("MailboxName")
inbox = outlook.Folders.Item(1).Folders['Inbox']

# TODO - Code login function to grab user apiKey ( & Store/Remember it?)
apiKey = ('')

apiUrl = "https://api.monday.com/v2"
headers = {"Authorization": apiKey}
monday = MondayClient(apiKey)

query_boards = '{ boards (limit:5) {name id} }'

def get_current_user():
    query_current_user = 'query { me {name} }'
    data = {'query': query_current_user}
    r = requests.post(url=apiUrl, json=data, headers=headers)
    data = r.json()
    current_user = (data['data']['me']['name'])
    print(current_user)
    return current_user

def get_unread():
    return

def filter_alerts():
    return

# Sort alerts (Covid, SQL, etc)
def sort_alerts():
    return

# Handle alert mail in Outlook
def ol_handle_alerts():
    return

# Handle alert mail on monday.com
def monday_handle_alerts():
    return

# Sync Outlook and monday.com inboxes
def mailsync():
    return
