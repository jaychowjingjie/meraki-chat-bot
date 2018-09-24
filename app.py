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
import re
import emotions
import verification
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

    #print ("Data from webhook:")
    #print (json.dumps(data, indent=4))

    #print ("\nHeaders from webhook:")
    #print (headers)
    #print ('type:',type(headers))

    #print ("Actor ID", data['actorId'])

    # If the poster of the message was NOT the bot itself
    if data['actorId'] != bot_id:
        spark_headers = set_headers(bot_token)

        # Get more specific information about the message that triggered the webhook
        json_string = get_message_details(spark_headers, messageID)
        message = json.loads(json_string)

        print ("\n\nMessage Details: ")
        print (json.dumps(message, indent=4))

        ####### Your main business logic goes here #######
        # shut off guest network during a specific timing, so no abuse #
        # meraki is plug and play, people buying your idea #
        # do something rudimentary, then have the road map #
        # quantify the use cases and impacts #
        if message['text'] == "hi" or message['text'] == "hey":
            post_message_to_room(spark_headers, roomID, "Hey, I am test_meraki bot! I can do emotion analysis and immediate intruder alert. 1) For emotion analysis, say something like \"how many people at MV camera 1 had a happy index of above 0.5 from noon to midnight yesterday?\" 2) For immediate intruder alert, say \"start monitoring\". You can also try other commands like \"show me the picture caught on MV camera 1 yesterday at 7pm\"")
        if message['text'] == "how many people at MV camera 1 had a happy index of above 0.5 from noon to midnight yesterday?":
            ret_value = emotions.emotion_details(1200, 2400, "happy", 0.5)
        #if not (re.search(".*(happy|sad|angry|neutral).*\.(\d).* from (\d*) to (\d*)", message['text'])):
            #parsed_string==re.search(".*(happy|sad|angry|neutral).*\.(\d).* from (\d*) to (\d*)", message['text'])
            #index=0
            #index=0.1*float(parsed_string.group(2))
            #ret_value = emotions.emotion_details(parsed_string.group(3), parsed_string.group(4), parsed_string.group(1), index)

            numMatched = ret_value[0]
            total = ret_value[1]
            # print("ret value", ret_value)
            post_message_to_room(spark_headers,roomID, str(numMatched) + " out of " + str(total) + " people(retreived from Meraki MV's API)")
        if message['text'] == "tell me more about myself as a user":
            post_message_to_room(spark_headers,roomID,json.dumps(message))
        if message['text'] == "what is my email" or message['text'] == "who am i":
            post_message_to_room(spark_headers,roomID, message["personEmail"])
        if message['text'] == "what is this message id":
            post_message_to_room(spark_headers,roomID, message["id"])
        if message['text'] == "what is this room id":
            post_message_to_room(spark_headers,roomID, message["roomId"])
        if message['text'] == "what is my person id":
            post_message_to_room(spark_headers,roomID, message["personId"])
        if message['text'] == "when was this message created":
            post_message_to_room(spark_headers,roomID, message["created"])
        if message['text'] == "do you love cisco":
            post_message_to_room(spark_headers,roomID, "I love cisco")
        if message['text'] == "show me the picture caught on MV camera 1 yesterday at 7pm":
            post_message_to_room(spark_headers,roomID, "Here is the weblink to access the photo taken from MV camera 1: https://media.gq.com/photos/56436afea3bd50211a99c42d/master/w_800/obama-gq-1215-05.jpg")
        #if message['text'] == "help":
            #post_message_to_room(spark_headers,roomID, "Things to say: \"hi\", \"tell me more about myself as a user\", \"what is my email\", \"what is this message id\", \"what is this room id\", "what is my person id", "when was this message created", "do you love cisco")
        if message['text'] == "start monitoring":
            res = verification.start_monitoring()
            post_message_to_room(spark_headers,roomID, res[0])
            post_message_to_room(spark_headers, roomID, "I have captured the face(retreived from Meraki MV's API) here at  " + res[1] + ". Please reply \"1\" for me to call the police immediately. Otherwise, reply \"2\" for me to ignore this.")
        if message['text'] == "1":
            post_message_to_room(spark_headers, roomID, "I have called the police...they're on the way now. Please remain calm.")
        if message['text'] == "2":
            post_message_to_room(spark_headers, roomID, "Ignored. Have a good day ahead.")

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
