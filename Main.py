from defs import Client
from Credentials import twilio_get_sid, twilio_get_number, twilio_get_auth

gpt_requests = 0
weather_requests = 0
translate_requests = 0
command_count = 0
valid_command_count = 0
client = Client(twilio_get_number(), twilio_get_sid(), twilio_get_auth())
day_limit = 15

if __name__ == "__main__":
    import asyncio
    import time

    import Credentials
    import defs
    from commands.Command_Admin import admin_command
    from commands.Command_Help import help_command
    from commands.Command_Weather import v1weather, v2weather
    from commands.Command_QR import qr_command
    from commands.Command_Status import status_command
    from commands.Command_Secret import secret_command
    from commands.Command_Details import details_command
    from commands.Command_GPT import gpt_command
    from commands.Command_Translate import translate_command
    from commands.Command_Dictionary import dict_command
    from commands.Command_bulletin import bulletin_command
    from commands.Command_Patron import add_patron, patron_list, msg_json

    # initialization

    client = defs.Client(Credentials.twilio_get_number(), Credentials.twilio_get_sid(), Credentials.twilio_get_auth())
    list1 = []

    error_message = "ERROR:UNKNOWN_COMMAND. Please check spelling."
    print("Running Program.")

    # marks all messages sent while bot was down as read, notifies them of online status

    messages = client.get_unread_messages(50)
    for message in messages:
        if message.number not in list1:
            message.send_sms("Service is now back online.")
            list1.append(message.number)
        message.mark_as_read()

    # message handler

    while True:

        # if the time is midnight and 00 minutes

        if time.strftime("%H%M", time.localtime()) == "2300":
            msg_json = {}

        messages = client.get_unread_messages(3)
        for msg in messages:
            msg.mark_as_read()
            if msg.content[0] == "!":

                # increment command count for that user

                if msg.number in msg_json.keys():
                    msg_json[msg.number] += 1
                else:
                    msg_json.update({msg.number: 1})

                if msg_json[msg.number] < day_limit or msg.number in patron_list:

                    command_count += 1
                    valid_command_count += 1
                    message_content = msg.content
                    if str.lower(message_content) == "!v1weather":
                        print(f"command activated: v1weather       {time.strftime('%H:%M', time.localtime())}")
                        asyncio.run(v1weather(msg))

                    elif str.lower(message_content) == "!weather" or str.lower(message_content) == "!v2weather":
                        print(f"command activated: weather       {time.strftime('%H:%M', time.localtime())}")
                        asyncio.run(v2weather(msg))

                    elif str.lower(message_content)[:5] == "!help":
                        print(f"command activated: help       {time.strftime('%H:%M', time.localtime())}")
                        asyncio.run(help_command(msg, message_content))

                    elif str.lower(message_content) == "!details":
                        print(f"command activated: details       {time.strftime('%H:%M', time.localtime())}")
                        asyncio.run(details_command(msg))

                    elif str.lower(message_content) == "!status":
                        print(f"command activated: status       {time.strftime('%H:%M', time.localtime())}")
                        asyncio.run(status_command(msg))

                    elif str.lower(message_content) == "!secret":
                        print(f"command activated: secret       {time.strftime('%H:%M', time.localtime())}")
                        asyncio.run(secret_command(msg))

                    elif str.lower(message_content) == "!admin":
                        print(f"command activated: admin       {time.strftime('%H:%M', time.localtime())}")
                        asyncio.run(admin_command(msg))

                    elif str.lower(message_content) == "!gpt" or str.lower(message_content) == "!chatgpt":
                        print(f"command activated: gpt       {time.strftime('%H:%M', time.localtime())}")
                        asyncio.run(gpt_command(msg))

                    elif str.lower(message_content) == "!qr" or str.lower(message_content) == "!qrcode":
                        print(f"command activated: qr code       {time.strftime('%H:%M', time.localtime())}")
                        asyncio.run(qr_command(msg))

                    elif str.lower(message_content) == "!translate":
                        print(f"command activated: translate       {time.strftime('%H:%M', time.localtime())}")
                        asyncio.run(translate_command(msg))

                    elif str.lower(message_content) == "!dictionary":
                        print(f"command activated: dictionary       {time.strftime('%H:%M', time.localtime())}")
                        asyncio.run(dict_command(msg))

                    elif str.lower(message_content) == "!bulletin" or str.lower(message_content) == "!news":
                        print(f"command activated: bulletin       {time.strftime('%H:%M', time.localtime())}")
                        bulletin_command(msg)

                    elif str.lower(message_content) == "!patron" or str.lower(message_content) == "!add":
                        print(f"command activated: patron       {time.strftime('%H:%M', time.localtime())}")
                        asyncio.run(add_patron(msg))

                    elif str.lower(message_content) == "!test":
                        if msg.number in patron_list:
                            msg.send_sms("You are in the patron list.")
                        else:
                            msg.send_sms("You are not in the patron list.")

                    # if command is invalid

                    else:
                        print(f'Unknown command "{message_content}" {time.strftime("%H:%M", time.localtime())}')
                        valid_command_count -= 1
                        msg.send_sms(error_message)


                else:
                    msg.send_sms(f"You have reached your limit of commands for the day ({day_limit}). Sign up on our patreon here to become a Premium Member: patreon.com/Eth0sSMSOfficialPatreon")

        # how often to check for new messages. I have found this is the most stable, keep on this number if you can.

        time.sleep(.5)
