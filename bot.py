import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
from templates import *
from database import *
import json

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SLACK_SIGNING_SECRET'],'/slack/events', app)
client = slack.WebClient(token=os.environ['SLACK_BOT_TOKEN'])



@app.route('/help', methods=['POST'])
def help():
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get("channel_id")
    client.chat_postEphemeral(channel=channel_id, user=user_id, text=help_message)
    return Response(), 200

@app.route('/takedownform', methods=['POST'])
def takedownform():
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get("channel_id")
    client.chat_postEphemeral(channel=channel_id, user=user_id, text="Testing", blocks=takedown_form)
    return Response(), 200

@app.route('/cleanupsettings', methods=['POST'])
def cleanupsettings():
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get("channel_id")
    client.chat_postEphemeral(channel=channel_id, user=user_id, text="Testing", blocks=cleanup_settings_form)
    return Response(), 200

@app.route('/userform', methods=['POST'])
def userform():
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get("channel_id")
    print(channel_id)
    client.chat_postEphemeral(channel=channel_id, user=user_id, text="Testing", blocks=user_form)
    return Response(), 200

@app.route('/removeuser', methods=['POST'])
def removeuser():
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get("channel_id")
    client.chat_postEphemeral(channel=channel_id, user=user_id, text="Testing", blocks=remove_user_form)
    return Response(), 200


@app.route('/interactions', methods=['POST'])
def interactions():
    data = json.loads(request.form.get("payload"))
    action = data["actions"][0]["action_id"]
    if action == "actionId-takedownsubmit":
        slack_id = data["user"]["id"]
        input_keys = list(data["state"]["values"])
        name = data["state"]["values"][input_keys[0]]["plain_text_input-action"]["value"]
        membership = data["state"]["values"][input_keys[1]]["static_select-action"]["selected_option"]["text"]["text"]
        user = (name, membership, slack_id)
        days = data["state"]["values"][input_keys[2]]["takedowns-action"]["selected_options"]
        takedown = [0,0,0,0,0,0,0,0,0,0,membership,slack_id]
        for day in days:
            if day["value"] == "value-ML":
                takedown[0] = 1
            elif day["value"] == "value-MD":
                takedown[1] = 1
            elif day["value"] == "value-TL":
                takedown[2] = 1
            elif day["value"] == "value-TD":
                takedown[3] = 1
            elif day["value"] == "value-WL":
                takedown[4] = 1
            elif day["value"] == "value-WD":
                takedown[5] = 1
            elif day["value"] == "value-RL":
                takedown[6] = 1
            elif day["value"] == "value-RD":
                takedown[7] = 1
            elif day["value"] == "value-FL":
                takedown[8] = 1
            elif day["value"] == "value-FD":
                takedown[9] = 1
        add_user(conn, user)
        add_takedown(conn, takedown)
    elif action == "actionId-usersubmit":
        slack_id = data["user"]["id"]
        input_keys = list(data["state"]["values"])
        name = data["state"]["values"][input_keys[0]]["plain_text_input-action"]["value"]
        membership = data["state"]["values"][input_keys[1]]["static_select-action"]["selected_option"]["text"]["text"]
        user = (slack_id, name, membership)
        add_user(conn, user)
    elif action == "actionId-removesubmit":
        input_keys = list(data["state"]["values"])
        slack_id = data["state"]["values"][input_keys[0]]["users_select-action"]["selected_user"]
        remove_user(conn, slack_id)
    elif action == "actionId-cleanupsettingssubmit":
        slack_id = data["user"]["id"]
        input_keys = list(data["state"]["values"])
        cleanupName = data["state"]["values"][input_keys[0]]["plain_text_input-action"]["value"]
        deck = data["state"]["values"][input_keys[1]]["static_select-action"]["selected_option"]["value"]
        townsman = data["state"]["values"][input_keys[2]]["radio_buttons-action"]["selected_option"]["value"]
        minimumInHouse = data["state"]["values"][input_keys[3]]["plain_text_input-action"]["value"]
        minimumPeople = data["state"]["values"][input_keys[4]]["plain_text_input-action"]["value"]
        cleanup = (cleanupName, deck, townsman, minimumInHouse, minimumPeople)
        add_cleanup(conn, cleanup)
    elif action == "actionId-cleanupsettingremove":
        slack_id = data["user"]["id"]
        input_keys = list(data["state"]["values"])
        cleanupName = data["state"]["values"][input_keys[0]]["plain_text_input-action"]["value"]
        remove_cleanup(conn, cleanupName)
    return Response(), 200

@app.route('/generate-cleanup-database', methods=['POST'])
def generatecleanupdatabase():
    generate_cleanups_database(conn)
    return Response(), 200

@app.route('/generate-cleanups', methods=['POST'])
def generatecleanups():
    generate_cleanups(conn)
    return Response(), 200

@app.route('/generate-takedowns', methods=['POST'])
def generatetakedowns():
    status = generate_takedown(conn)
    print(status)
    return Response(), 200



if __name__ == "__main__":
    conn = create_connection(os.getcwd()+"\\thetabot.db")
    if conn is not None:
        startup(conn)
    else:
        print("Welp Fuck")
    app.run(debug=True, port=8080)