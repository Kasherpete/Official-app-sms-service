import time
from main import Main_Command_Handler
import pytextnow as pytn
import Credentials
import asyncio

# client initialization

username = Credentials.username()
sid = Credentials.sid()
csrf = Credentials.csrf()
client = pytn.Client(username, sid_cookie=sid, csrf_cookie=csrf)


async def ask(question, msg, timeout, default):
    timer_timeout = time.perf_counter()
    msg.send_sms(question)
    while time.perf_counter() - timer_timeout <= timeout:
        await asyncio.sleep(1)
        new_messages = Main_Command_Handler.client.get_unread_messages()
        for message in new_messages:
            if message.number == msg.number:
                message.mark_as_read()
                return message.content

    # timeout error messages
    await asyncio.sleep(1)
    if default != "":
        msg.send_sms(f"ERROR:TIMEOUT. User took too long to respond. Default response: {default}")
    else:
        msg.send_sms("ERROR:TIMEOUT. User took too long to respond. No default response, command terminated.")
    return default
