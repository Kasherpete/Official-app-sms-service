import Main
import pytextnow as pytn
import Credentials
import asyncio
import pytextnow
import time

# client initialization

username = Credentials.username()
sid = Credentials.sid()
csrf = Credentials.csrf()
client = pytn.Client(username, sid_cookie=sid, csrf_cookie=csrf)


last_msg_sent = 0


async def ask(question, msg, timeout, default):

    timer_timeout = time.perf_counter()
    msg.send_sms(question)

    while time.perf_counter() - timer_timeout <= timeout:

        await asyncio.sleep(1)
        new_messages = Main.client.get_unread_messages()

        for message in new_messages:

            if message.number == msg.number:
                message.mark_as_read()
                return message.content

    # timeout error messages

    await asyncio.sleep(1)
    if default != "":
        msg.send_sms(f'ERROR:TIMEOUT. User took too long to respond. Default response: {default}.')
    else:
        msg.send_sms("ERROR:TIMEOUT. User took too long to respond. Please use command again to retry.")
    return default


def send_sms(content, msg):
    sleep_time = time.time() - last_msg_sent + 2
    if (sleep_time > 0):
        time.sleep(sleep_time)
    sms_limit = 450

    content = content.replace("\n", '      ')
    content = content.replace('"', '*')
    list_response = [content[i:i + sms_limit] for i in
                     range(0, len(content), sms_limit)]


    for message in list_response:
        time.sleep(4)

        try:
            last_msg_sent = time.time()
            msg.send_sms(message)
        except pytextnow.error.FailedRequest:
            print(
                "ERROR:INVALID_CHAR. Sorry, there was an error sending a message. This is a known bug and is currently being worked on.")
            msg.send_sms(
                "ERROR:INVALID_CHAR. Sorry, there was an error sending a message. This is a known bug and is currently being worked on.")


# this function is a copy of the sms.ask, but it returns the message class instead of str

async def ask_advanced(question, msg, timeout, default):

    timer_timeout = time.perf_counter()
    msg.send_sms(question)

    while time.perf_counter() - timer_timeout <= timeout:

        await asyncio.sleep(1)
        new_messages = Main.client.get_unread_messages()

        for message in new_messages:

            if message.number == msg.number:
                message.mark_as_read()
                return message  # <-- here is the difference

    # timeout error messages

    await asyncio.sleep(1)
    if default != "":
        msg.send_sms(f'ERROR:TIMEOUT. User took too long to respond. Default response: {default}.')
    else:
        msg.send_sms("ERROR:TIMEOUT. User took too long to respond. Please use command again to retry.")
    return default