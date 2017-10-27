#
#   Hantzley Tauckoor (htauckoo@cisco.com)
#       October 2017
#
#       This sample Spark bot application uses ngrok to facilitate a webhook to Spark
#
#
#   REQUIREMENTS:
#       Flask python module
#       ngrok - https://ngrok.com/
#       Spark account with Bot created
#       Spark webhook created with bot token
#       settings.py file, you can modify and rename settings_template.py
#
#   WARNING:
#       This script is meant for educational purposes only.
#       Any use of these scripts and tools is at
#       your own risk. There is no guarantee that
#       they have been through thorough testing in a
#       comparable environment and we are not
#       responsible for any damage or data loss
#       incurred with their use.
#


import requests
from flask import Flask, request, session, redirect
import json
import settings
import logging
logging.basicConfig(level=logging.DEBUG)

from settings import bot_id, bot_token, ngrok_url, webhook_id, webhook_name

# get ngrok tunnels information
def get_ngrok_tunnels(ngrok_url):
    headers = {'cache-control': "no-cache"}
    response = requests.request("GET", ngrok_url, headers=headers)
    tunnels = response.json()
    return {
        'public_http_url' : tunnels['tunnels'][0]['public_url'],
        'public_https_url' : tunnels['tunnels'][1]['public_url']
    }

# set spark headers
def set_headers(access_token):
    accessToken_hdr = 'Bearer ' + access_token
    spark_header = {
        'Authorization':accessToken_hdr,
        'Content-Type':'application/json; charset=utf-8',
        }
    return (spark_header)

# update webhook with updated ngrok tunnel information
def update_webhook (the_headers,webhook_name,webhook_id,targetUrl):
    url = "https://api.ciscospark.com/v1/webhooks/" + webhook_id
    payload = "{\n\t\"name\": \"" + webhook_name + "\",\n\t\"targetUrl\": \"" + targetUrl + "\"\n}"
    response = requests.request("PUT", url, data=payload, headers=the_headers)
    return response.status_code

# posts a message to the room
def post_message_to_room(the_header,roomId,msg):
    message = {"roomId":roomId,"markdown":msg}
    uri = 'https://api.ciscospark.com/v1/messages'
    resp = requests.post(uri, json=message, headers=the_header)

# get message details
def get_message_details(the_header,msgId):
    uri = 'https://api.ciscospark.com/v1/messages/' + msgId
    resp = requests.get(uri, headers=the_header)
    return resp.text


#### Business logic functions goes here


# Flask used as listener for webhooks from Spark
app = Flask(__name__)

@app.route('/',methods=['POST'])
def listener():
    # On receipt of a POST (webhook), load the JSON data from the request
    data = json.loads(request.data)
    headers = request.headers

    #print data
    messageID = data['data']['id']
    roomID = data['data']['roomId']

    print ("Data from webhook:")
    print (json.dumps(data, indent=4))

    print ("\nHeaders from webhook:")
    print (headers)
    print ('type:',type(headers))


    # If the poster of the message was NOT the bot itself
    if data['actorId'] != bot_id:
        spark_headers = set_headers(bot_token)

        # Get more specific information about the message that triggered the webhook
        json_string = get_message_details(spark_headers, messageID)
        message = json.loads(json_string)

        print ("\n\nMessage details: ")
        print (json.dumps(message, indent=4))

        ####### Your main business logic goes here #######

    return "OK"


# Runs the listener
if __name__ == '__main__':
    #get ngrok tunnel details and update webhook
    print ("Updating webhook with ngrok tunnel details")
    headers = set_headers(bot_token)
    ngrok_tunnels = get_ngrok_tunnels(ngrok_url)
    public_url = ngrok_tunnels['public_http_url'] # to use https, use the 'public_https_url' key instead
    print ("Webhook update status code: ", update_webhook(headers, webhook_name, webhook_id, public_url))

    #launching main application
    print ("Launching spark bot application")
    app.run(host='0.0.0.0', port=8080, debug=True)
