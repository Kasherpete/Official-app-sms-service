import pytextnow as pytn
import Credentials

# client initialization

username = Credentials.username()
sid = Credentials.sid()
csrf = Credentials.csrf()
client = pytn.Client(username, sid_cookie=sid, csrf_cookie=csrf)


async def help_command(msg):
    msg.send_sms("The current commands are: !weather, !help, !details, !status.")

