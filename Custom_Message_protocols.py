from Main import client
from asyncio import sleep
from time import perf_counter, sleep


async def ask(question, msg, timeout, default):
    timer_timeout = perf_counter()
    msg.send_sms(question)

    while perf_counter() - timer_timeout <= timeout:
        await sleep(1)
        new_messages = client.get_unread_messages(6)  # idk why I make it this number, it seems best for high capacity

        for message in new_messages:

            if message.number == msg.number:
                message.mark_as_read()
                return message.content

    # timeout error messages

    await sleep(1)
    if default != "":
        msg.send_sms(f'ERROR:TIMEOUT. User took too long to respond. Default response: {default}.')
    else:
        msg.send_sms("ERROR:TIMEOUT. User took too long to respond. Please use command again to retry.")
    return default


def send_sms(content, msg):
    sms_limit = 1550

    list_response = [content[i:i + sms_limit] for i in
                     range(0, len(content), sms_limit)]

    for message in list_response:
        msg.send_sms(message)
        sleep(3)


# this function is a copy of the sms.ask, but it returns the message class instead of str

async def ask_advanced(question, msg, timeout, default):
    timer_timeout = perf_counter()
    msg.send_sms(question)

    while perf_counter() - timer_timeout <= timeout:
        await sleep(1)
        new_messages = client.get_unread_messages(6)

        for message in new_messages:

            if message.number == msg.number:
                message.mark_as_read()
                return message

    # timeout error messages

    await sleep(1)
    if default != "":
        msg.send_sms(f'ERROR:TIMEOUT. User took too long to respond. Default response: {default}.')
    else:
        msg.send_sms("ERROR:TIMEOUT. User took too long to respond. Please use command again to retry.")
    return default
