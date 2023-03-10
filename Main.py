from defs import Client
from Credentials import twilio_get_sid, twilio_get_number, twilio_get_auth

gpt_requests = 0
weather_requests = 0
translate_requests = 0
client = Client(twilio_get_number(), twilio_get_sid(), twilio_get_auth())

if __name__ == "__main__":
    import asyncio
    import time

    import Credentials
    import defs
    from commands.Command_Admin import command_count, valid_command_count, admin_command
    from commands.Command_Help import help_command
    from commands.Command_Weather import weather
    from commands.Command_QR import qr_command
    from commands.Command_Status import status_command
    from commands.Command_Secret import secret_command
    from commands.Command_Details import details_command
    from commands.Command_GPT import gpt_command
    from commands.Command_Translate import translate_command
    from commands.Command_Dictionary import dict_command
    from commands.Command_bulletin import bulletin_command

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
        messages = client.get_unread_messages(3)
        for msg in messages:
            msg.mark_as_read()
            if msg.content[0] == "!":
                command_count += 1
                valid_command_count += 1
                message_content = msg.content

                if str.lower(message_content) == "!weather":
                    print("command activated: weather")
                    asyncio.run(weather(msg))

                elif str.lower(message_content)[:5] == "!help":
                    print("command activated: help")
                    asyncio.run(help_command(msg, message_content))

                elif str.lower(message_content) == "!details":
                    print("command activated: details")
                    asyncio.run(details_command(msg))

                elif str.lower(message_content) == "!status":
                    print("command activated: status")
                    asyncio.run(status_command(msg))

                elif str.lower(message_content) == "!secret":
                    print("command activated: secret")
                    asyncio.run(secret_command(msg))

                elif str.lower(message_content) == "!admin":
                    print("command activated: admin")
                    asyncio.run(admin_command(msg))

                elif str.lower(message_content) == "!gpt" or str.lower(message_content) == "!chatgpt":
                    print("command activated: gpt")
                    asyncio.run(gpt_command(msg))

                elif str.lower(message_content) == "!qr" or str.lower(message_content) == "!qrcode":
                    print("command activated: qr code")
                    asyncio.run(qr_command(msg))

                elif str.lower(message_content) == "!translate":
                    print("command activated: translate")
                    asyncio.run(translate_command(msg))

                elif str.lower(message_content) == "!dictionary":
                    print("command activated: dictionary")
                    asyncio.run(dict_command(msg))

                elif str.lower(message_content) == "!bulletin" or str.lower(message_content) == "!news":
                    print("command activated: bulletin")
                    bulletin_command(msg)

                # if command is invalid

                else:
                    print(f'Unknown command "{message_content}".')
                    valid_command_count -= 1
                    msg.send_sms(error_message)

        # how often to check for new messages. I have found this is the most stable, keep on this number if you can.

        time.sleep(.5)
