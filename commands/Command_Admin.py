import pytextnow as pytn
import Credentials
import Custom_Message_protocols as sms
import asyncio

# client initialization


username = Credentials.username()
sid = Credentials.sid()
csrf = Credentials.csrf()
client = pytn.Client(username, sid_cookie=sid, csrf_cookie=csrf)


async def admin_command(msg):
    password = await sms.ask("ENTER PASSWORD", msg, 60, "")
    if password == Credentials.admin_password():

        msg.send_sms("Correct password. This command is currently in development.")
    else:
        msg.send_sms("Incorrect password. User locked for one minute.")
        await asyncio.sleep(60)
