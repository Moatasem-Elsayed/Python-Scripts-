# # Download the helper library from https://www.twilio.com/docs/python/install
# import os
# from twilio.rest import Client
#
#
# # Your Account Sid and Auth Token from twilio.com/console
# # and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
# client = Client()
#
# message = client.messages.create(
#                               body='Hello there!',
#                               from_='whatsapp:+16469564368',
#                               to='whatsapp:+201112932885'
#                           )
#
# # print(os.environ['TWILIO_ACCOUNT_SID'])