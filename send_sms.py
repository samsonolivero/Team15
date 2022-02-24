# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# Make sure to add echo "twilio.env" >> .gitignore
account_sid = os.environ['AC8755789b0266e05e0e26ad395953a72d']
auth_token = os.environ['e46bd1838e39b5f5403a28139446aefc']
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+19036257614',
         media_url=['https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg'],
         to='+14056581239'
     )

print(message.sid)


