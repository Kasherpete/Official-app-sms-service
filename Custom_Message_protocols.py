from Main import client
import asyncio
import time


async def ask(question, msg, timeout, default):

    timer_timeout = time.perf_counter()
    msg.send_sms(question)

    while time.perf_counter() - timer_timeout <= timeout:
        await asyncio.sleep(1)
        new_messages = client.get_unread_messages(2)

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
    msg.send_sms(content)


# this function is a copy of the sms.ask, but it returns the message class instead of str

async def ask_advanced(question, msg, timeout, default):

    timer_timeout = time.perf_counter()
    msg.send_sms(question)

    while time.perf_counter() - timer_timeout <= timeout:
        await asyncio.sleep(1)
        new_messages = client.get_unread_messages(2)

        for message in new_messages:

            if message.number == msg.number:
                message.mark_as_read()
                return message