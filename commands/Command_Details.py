import pytextnow as pytn
import Credentials

# client initialization

username = Credentials.username()
sid = Credentials.sid()
csrf = Credentials.csrf()
client = pytn.Client(username, sid_cookie=sid, csrf_cookie=csrf)


# TODO: update version number when making new release on GitHub
async def details_command(msg):
    msg.send_sms("This service is being hosted and developed by @Kasherpete#2661, @Jopes#6969 <--(Idiot), and @SpaceSaver2000#2992. Message them on discord for any questions/feedback. Thanks to SpaceSaver for hosting the service, Kasherpete for adding ChatGPT, and jopes for having the original idea, this would not be possible without their help. Version 1.3.31")
