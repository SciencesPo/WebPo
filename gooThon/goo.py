#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

BASEDIR = os.getcwd()
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = BASEDIR + '/WebPo/gooThon/client_secret.json'
APPLICATION_NAME = 'Drive API Python Quickstart'

def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'drive-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main(what, id, mime):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)
    if what is 'settings':
        r = service.files().export(fileId=id,mimeType='text/csv').execute()
        return r
    elif what is 'content':
        content = service.files().export(fileId=id,mimeType=mime).execute()
        return content
    else:
        qstr="'"+id.strip()+"' in parents"
        r = service.files().list(q=qstr, fields="files(id, name)").execute()
        items = r.get('files', [])
        for i in items:
            f = service.files().get(fileId=i['id']).execute()
            i['mime'] = f['mimeType']

        return items


if __name__ == '__main__':
    main()