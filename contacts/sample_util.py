from twilio.rest import Client
from .scrape import get_memes
account_sid = "" # Enter your twilio account sid
auth_token = "" # Enter your twilio auth token
client = Client(account_sid, auth_token)
call = get_memes()
def send_whatsapp_message(body, to):
    for i in range(len(call)):
        message = client.messages.create(
                                      body=body,
                                      from_='whatsapp:+14155238886',
                                      to=f'whatsapp:{to}',
                                    media_url = f"{call[i]}"
                                  )

        print(message.sid)


