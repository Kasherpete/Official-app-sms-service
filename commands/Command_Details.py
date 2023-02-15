import pytextnow as pytn
import Credentials

# client initialization

username = Credentials.username()
sid = Credentials.sid()
csrf = Credentials.csrf()
client = pytn.Client(username, sid_cookie=sid, csrf_cookie=csrf)


async def details_command(msg):
    msg.send_sms("This service is being hosted and developed by @Jopes#6969, @SpaceSaver2000#2992, and @Kasherpete#2661. Message them on discord for any questions/feedback. Version 1.2.0")