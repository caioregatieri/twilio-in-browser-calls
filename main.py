from flask import Flask, render_template, jsonify
from flask import request
 
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VoiceGrant
from twilio.twiml.voice_response import VoiceResponse, Dial

from flask_cors import CORS 
from dotenv import load_dotenv
import os
import pprint as p

load_dotenv()

account_sid = os.environ['TWILIO_ACCOUNT_SID']
api_key = os.environ['TWILIO_API_KEY_SID']
api_key_secret = os.environ['TWILIO_API_KEY_SECRET']
twiml_app_sid = os.environ['TWIML_APP_SID']
twilio_number = os.environ['TWILIO_NUMBER']

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    # template_dir = os.path.abspath('./templates/home.html')
    return render_template(
        'index.html',
        title="In browser calls",
    )

@app.route('/token', methods=['GET'])
def token():
    identity = twilio_number
    outgoing_application_sid = twiml_app_sid

    access_token = AccessToken(
        account_sid, 
        api_key, 
        api_key_secret, 
        identity=identity
    )

    voice_grant = VoiceGrant(
        outgoing_application_sid=outgoing_application_sid,
        incoming_allow=True,
    )
    access_token.add_grant(voice_grant)

    response = jsonify({'token': access_token.to_jwt().decode(), 'identity': identity})

    return response

#https://demo.twilio.com/welcome/voice/

@app.route('/handle_calls', methods=['POST'])
def handle_calls():
    p.pprint(request.form)
    response = VoiceResponse()
    dial = Dial(callerId=twilio_number)

    if 'To' in request.form and request.form['To'] != twilio_number:
        print('outbound call')
        dial.number(request.form['To'])
        return str(response.append(dial))

    return ''

@app.route('/fallback', methods=['POST'])
def fallback():
    p.pprint(request.form)

    return ''

@app.route('/status_callback', methods=['POST'])
def status_callback():
    p.pprint(request.form)
    
    return ''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)