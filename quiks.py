from flask import Flask
from eve import Eve
from eve.auth import BasicAuth
import dropbox
import time
import os

#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/senddata', methods=['POST'])
def upload_data():
    # Get your app key and secret from the Dropbox developer website
    app_key = 'wkbpkn13tc7zmew'
    app_secret = 'qqjx29o4ctunmo5'
    flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
    #Use this only if we want to upload to third party Dropbox account. Otherwise use our access token below
    # Have the user sign in and authorize this token
    #authorize_url = flow.start()
    #print ('1. Go to: ' + authorize_url)
    #print ('2. Click "Allow" (you might have to log in first)')
    #print ('3. Copy the authorization code.')
    #code = input("Enter the authorization code here: ").strip()
    #access_token, user_id = flow.finish(code)
    # This will fail if the user enters an invalid authorization code


    access_token = 'UdQIYgVxjdAAAAAAAAAAHze8SuNXW5mycFPEdcWl1eYj0KG0GJFGu-je18XlvvWo'
    client = dropbox.client.DropboxClient(access_token)
    print ('linked account: ', client.account_info())

    #create temp file
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = 'scanfile' + timestr + '.txt'
    file = open(filename,"w")

    file.write('Hello World')
    file.write('This is our new text file')
    file.close()

    #upload temp file
    f = open(filename, 'rb')
    response = client.put_file('/' + filename, f)
    print ('uploaded: ', response)
    #remote temp file
    os.remove(filename)

    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)


