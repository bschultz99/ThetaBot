# pylint: disable=assignment-from-no-return, line-too-long
"""Bot Code"""
import os
from pathlib import Path
import json
import ssl
from threading import Thread
from dotenv import load_dotenv
from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
import slack
import requests
from templates import USER_FORM, REMOVE_USER_FORM, CLEANUP_SETTINGS_FORM, ADMIN_ADD_FORM, FINE_FORM, RECONCILLIATION_FORM, HELP_MESSAGE
from database import admin_check, generate_cleanups, generate_cleanups_database, generate_takedown, display_cleanups, display_takedowns, end_semester, display_fines, display_reconcilliations, display_naughtylist, add_user, remove_user, add_cleanup, remove_cleanup, admin_add, fines, reconcilliations, create_connection, startup



env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SLACK_SIGNING_SECRET'],'/slack/events', app)
client = slack.WebClient(token=os.environ['SLACK_BOT_TOKEN'], ssl=ssl_context)

@app.route('/help', methods=['POST'])
def helpform():
    """Help Slack Command"""
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get("channel_id")
    client.chat_postEphemeral(channel=channel_id, user=user_id, text=HELP_MESSAGE)
    return Response(), 200

@app.route('/userform', methods=['POST'])
def userform():
    """Userform Slack Command"""
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get("channel_id")
    client.chat_postEphemeral(channel=channel_id, user=user_id, text="Testing", blocks=USER_FORM)
    return Response(), 200

@app.route('/cleanupsettings', methods=['POST'])
def cleanupsettings():
    """Cleanupsettings Slack Command"""
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get("channel_id")
    if admin_check(conn, user_id):
        client.chat_postEphemeral(channel=channel_id, user=user_id, text="Testing", blocks=CLEANUP_SETTINGS_FORM)
    else:
        client.chat_postEphemeral(channel=channel_id, user=user_id, text="Fuck You. You Shouldn't be here. $5 Fine.")
    return Response(), 200


@app.route('/removeuser', methods=['POST'])
def removeuser():
    """Removeuser Slack Command"""
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get("channel_id")
    if admin_check(conn, user_id):
        client.chat_postEphemeral(channel=channel_id, user=user_id, text="Testing", blocks=REMOVE_USER_FORM)
    else:
        client.chat_postEphemeral(channel=channel_id, user=user_id, text="Fuck You. You Shouldn't be here. $5 Fine.")
    return Response(), 200

@app.route('/generate-cleanup-database', methods=['POST'])
def generatecleanupdatabase():
    """Generate Cleanups Database Slack Command"""
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get("channel_id")
    if admin_check(conn, user_id):
        generate_cleanups_database(conn)
    else:
        client.chat_postEphemeral(channel=channel_id, user=user_id, text="Fuck You. You Shouldn't be here. $5 Fine.")
    return Response(), 200

@app.route('/generate-cleanups', methods=['POST'])
def generatecleanups():
    """Generate Cleanups Slack Command"""
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get("channel_id")
    if admin_check(conn, user_id):
        Thread(target=generate_cleanups, args=(conn, channel_id, client, os.environ['SLACK_BOT_MEMBER_ID'])).start()
    else:
        client.chat_postEphemeral(channel=channel_id, user=user_id, text="Fuck You. You Shouldn't be here. $5 Fine.")
    return Response(), 200

@app.route('/generate-takedowns', methods=['POST'])
def generatetakedowns():
    """Generate Takedowns Slack Command"""
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get("channel_id")
    if admin_check(conn, user_id):
        status = Thread(target=generate_takedown, args=(conn, channel_id, client, os.environ['SLACK_BOT_MEMBER_ID'])).start()
        if status:
            client.chat_postEphemeral(channel=channel_id, user=user_id, text= f"Error Generating cleanups Here is the sum count, evaluate and have members update availability. {status}")
    else:
        client.chat_postEphemeral(channel=channel_id, user=user_id, text="Fuck You. You Shouldn't be here. $5 Fine.")
    return Response(), 200

@app.route('/revert-takedowns', methods=['POST'])
def reverttakedowns():
    """Revert Takedowns Slack Command"""
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get("channel_id")
    if admin_check(conn, user_id):
        client.chat_postEphemeral(channel=channel_id, user=user_id, text="Fuck You. You Shouldn't be here. $5 Fine.")
        #Thread(target=revert_takedowns, args=(conn,)).start()
    else:
        client.chat_postEphemeral(channel=channel_id, user=user_id, text="Fuck You. You Shouldn't be here. $5 Fine.")
    return Response(), 200

@app.route('/test', methods=['POST'])
def test():
    """Testing Command"""
    #data = client.conversations_create(name="testchannel11", is_private = True)
    try:
        client.conversations_invite(channel="C05NA6NMX88", users="UCQMZA62E")
    except slack.errors.SlackApiError:
        print("Oh no i dont care")
    #members = client.conversations_members(channel='C05ML6VEKV1')
    #print(members['members'])#.remove(os.environ['SLACK_BOT_MEMBER_ID']))
    return Response(), 200

@app.route('/display-takedowns', methods=['POST'])
def displaytakedowns():
    """Display Takedowns Slack Command"""
    data = request.form
    user_id = data.get('user_id')
    Thread(target=display_takedowns, args=(conn, user_id, client)).start()
    return Response(), 200

@app.route('/display-cleanups', methods=['POST'])
def displaycleanups():
    """Display Cleanups Slack Command"""
    data = request.form
    user_id = data.get('user_id')
    Thread(target=display_cleanups, args=(conn, user_id, client)).start()
    return Response(), 200

@app.route('/admin-form', methods=['POST'])
def adminform():
    """Admin Form Slack Command"""
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get("channel_id")
    if admin_check(conn, user_id):
        client.chat_postEphemeral(channel=channel_id, user=user_id, text="Testing", blocks=ADMIN_ADD_FORM)
    else:
        client.chat_postEphemeral(channel=channel_id, user=user_id, text="Fuck You. You Shouldn't be here. $5 Fine.")
    return Response(), 200

@app.route('/end-semester', methods=['POST'])
def endsemester():
    """End Semester Slack Command"""
    data = request.form
    user_id = data.get('user_id')
    if admin_check(conn, user_id):
        end_semester(conn)
    return Response(), 200

@app.route('/fines-form', methods=['POST'])
def finesform():
    """Fines Form Slack Command"""
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get('channel_id')
    if admin_check(conn, user_id):
        client.chat_postEphemeral(channel=channel_id, user=user_id, text="Testing", blocks=FINE_FORM)
    else:
        client.chat_postEphemeral(channel=channel_id, user=user_id, text="Fuck You. You Shouldn't be here. $5 Fine.")
    return Response(), 200

@app.route('/reconcilliation-form', methods=['POST'])
def reconcilliationform():
    """Reconcilliation Form Slack Command"""
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get('channel_id')
    if admin_check(conn, user_id):
        client.chat_postEphemeral(channel=channel_id, user=user_id, text="Testing", blocks=RECONCILLIATION_FORM)
    else:
        client.chat_postEphemeral(channel=channel_id, user=user_id, text="Fuck You. You Shouldn't be here. $5 Fine.")
    return Response(), 200

@app.route('/display-fines', methods=['POST'])
def displayfines():
    """Display Fines Slack Command"""
    data = request.form
    user_id = data.get('user_id')
    Thread(target=display_fines, args=(conn, user_id, client)).start()
    return Response(), 200

@app.route('/display-reconcilliations', methods=['POST'])
def displayreconcilliations():
    """Display Reconcilliations Slack Command"""
    data = request.form
    user_id = data.get('user_id')
    Thread(target=display_reconcilliations, args=(conn, user_id, client)).start()
    return Response(), 200

@app.route('/display-naughtylist', methods=['POST'])
def naughtylist():
    """Display Naughty List Slack Command"""
    data = request.form
    user_id = data.get('user_id')
    Thread(target=display_naughtylist, args=(conn, user_id, client)).start()
    return Response(), 200

@app.route('/interactions', methods=['POST'])
def interactions():
    """Interactions for all Slack Commands"""
    data = json.loads(request.form.get("payload"))
    action = data["actions"][0]["action_id"]
    if action == "actionId-usersubmit":
        slack_id = data["user"]["id"]
        input_keys = list(data["state"]["values"])
        try:
            name = data["state"]["values"][input_keys[0]]["plain_text_input-action"]["value"]
        except KeyError:
            name = client.users_info(user=slack_id)['user']['real_name']
        if name is None:
            name = client.users_info(user=slack_id)['user']['real_name']
        print(data["state"]["values"][input_keys[1]])
        membership = data["state"]["values"][input_keys[1]]["static_select-action"]["selected_option"]["text"]["text"]
        user = (slack_id, name, membership)
        days = data["state"]["values"][input_keys[2]]["takedowns-action"]["selected_options"]
        takedowns = [0,0,0,0,0,0,0,0,0,0,membership,slack_id]
        for day in days:
            if day["value"] == "value-ML":
                takedowns[0] = 1
            elif day["value"] == "value-MD":
                takedowns[1] = 1
            elif day["value"] == "value-TL":
                takedowns[2] = 1
            elif day["value"] == "value-TD":
                takedowns[3] = 1
            elif day["value"] == "value-WL":
                takedowns[4] = 1
            elif day["value"] == "value-WD":
                takedowns[5] = 1
            elif day["value"] == "value-RL":
                takedowns[6] = 1
            elif day["value"] == "value-RD":
                takedowns[7] = 1
            elif day["value"] == "value-FL":
                takedowns[8] = 1
            elif day["value"] == "value-FD":
                takedowns[9] = 1
        Thread(target=add_user, args=(conn, user, takedowns)).start()
        requests.post(data["response_url"], json={'delete_original': True, 'text': ''}, timeout=10)
    elif action == "actionId-removesubmit":
        input_keys = list(data["state"]["values"])
        slack_id = data["state"]["values"][input_keys[0]]["users_select-action"]["selected_user"]
        Thread(target=remove_user, args=(conn, slack_id)).start()
        requests.post(data["response_url"], json={'delete_original': True, 'text': ''}, timeout=10)
    elif action == "actionId-cleanupsettingssubmit":
        slack_id = data["user"]["id"]
        input_keys = list(data["state"]["values"])
        cleanup_name = data["state"]["values"][input_keys[0]]["plain_text_input-action"]["value"]
        deck = data["state"]["values"][input_keys[1]]["static_select-action"]["selected_option"]["value"]
        townsman = 1 if data["state"]["values"][input_keys[2]]["radio_buttons-action"]["selected_option"]["value"] == 'True' else 0
        minimum_inhouse = data["state"]["values"][input_keys[3]]["plain_text_input-action"]["value"]
        minimum_people = data["state"]["values"][input_keys[4]]["plain_text_input-action"]["value"]
        cleanup = (cleanup_name, deck, townsman, minimum_inhouse, minimum_people)
        Thread(target=add_cleanup, args=(conn, cleanup)).start()
        requests.post(data["response_url"], json={'delete_original': True, 'text': ''}, timeout=10)
    elif action == "actionId-cleanupsettingremove":
        slack_id = data["user"]["id"]
        input_keys = list(data["state"]["values"])
        cleanup_name = data["state"]["values"][input_keys[0]]["plain_text_input-action"]["value"]
        Thread(target=remove_cleanup, args=(conn, cleanup_name)).start()
        requests.post(data["response_url"], json={'delete_original': True, 'text': ''}, timeout=10)
    elif action == "actionId-adminaddsubmit":
        input_keys = list(data["state"]["values"])
        position = data["state"]["values"][input_keys[0]]["static_select-action"]["selected_option"]["value"]
        name = data["state"]["values"][input_keys[1]]["users_select-action"]["selected_user"]
        Thread(target=admin_add, args=(conn, position, name)).start()
        requests.post(data["response_url"], json={'delete_original': True, 'text': ''}, timeout=10)
    elif action == "actionId-finesubmit":
        slack_id = data["user"]["id"]
        input_keys = list(data["state"]["values"])
        person = data["state"]["values"][input_keys[0]]['users_select-action']['selected_user']
        fine_date = data["state"]["values"][input_keys[1]]['datepicker-action']['selected_date']
        fine_type = data["state"]["values"][input_keys[2]]['static_select-action']['selected_option']['text']['text']
        reason = data["state"]["values"][input_keys[3]]['plain_text_input-action']['value']
        amount = data['state']['values'][input_keys[4]]['plain_text_input-action']['value']
        Thread(target=fines, args=(conn, person, fine_date, fine_type, reason, amount, slack_id, client)).start()
        requests.post(data["response_url"], json={'delete_original': True, 'text': ''}, timeout=10)
    elif action == "actionId-reconcilliationsubmit":
        slack_id = data["user"]["id"]
        input_keys = list(data["state"]["values"])
        person = data["state"]["values"][input_keys[0]]['users_select-action']['selected_user']
        recon_date = data["state"]["values"][input_keys[1]]['datepicker-action']['selected_date']
        recon_type = data["state"]["values"][input_keys[2]]['static_select-action']['selected_option']['text']['text']
        notes = data["state"]["values"][input_keys[3]]['plain_text_input-action']['value']
        amount = data['state']['values'][input_keys[4]]['plain_text_input-action']['value']
        Thread(target=reconcilliations, args=(conn, person, recon_date, recon_type, notes, amount, slack_id, client)).start()
        requests.post(data["response_url"], json={'delete_original': True, 'text': ''}, timeout=10)
    return Response(), 200

if __name__ == "__main__":
    conn = create_connection("./thetabot.db")
    if conn is not None:
        startup(conn)
    else:
        print("Welp Fuck")
    app.run(debug=True, port=8080)
