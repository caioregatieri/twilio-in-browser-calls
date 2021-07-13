# twilio-in-browser-calls

## set virtual enviroument
$ python3 -m venv venv
$ source venv/bin/activate

## install dependencies
$ pip install twilio flask python-dotenv

## cp .env file
$ cp .env.example .env

## start
$ python3 main.py

## in another console start ngrok
$ ngrok http 3000

## twilio documentation
https://www.twilio.com/blog/make-receive-phone-calls-browser-twilio-programmable-voice-python-javascript