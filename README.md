# twilio-in-browser-calls

# set virtual enviroument
$ python3 -m venv backend/venv
$ source venv/bin/activate

# install dependencies
$ pip install twilio flask python-dotenv

# cp .env file
$ cp backend/.env.example backend/.env

# start backend
$ cd backend
$ python3 main.py

# in another console start ngrok
$ ngrok http 3000