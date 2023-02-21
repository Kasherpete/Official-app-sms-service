import pytextnow as pytn
import Credentials

# client initialization

username = Credentials.username()
sid = Credentials.sid()
csrf = Credentials.csrf()
client = pytn.Client(username, sid_cookie=sid, csrf_cookie=csrf)



async def details_command(msg):
    # TODO: update version number when new release is made
    msg.send_sms("This service is being hosted and developed by @Kasherpete#2661, @Jopes#6969 <--(Idiot), and @SpaceSaver2000#2992. Message them on discord for any questions/feedback. Thanks to SpaceSaver for hosting the service, Kasherpete for adding ChatGPT, translate and other commands, and jopes for having and creating the original idea, this would not be possible without their help. If you have a suggestion or question, feel free to message (629) 240-4333. Version 1.4.32")
