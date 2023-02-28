import pytextnow as pytn

import Credentials
import asyncio
from commands import Command_Details, Command_Secret, Command_Status, Command_Weather, Command_Help, Command_Admin, Command_GPT, Command_QR, Command_Translate, Command_Dictionary, Command_bulletin

# client initialization

username = Credentials.username()
sid = Credentials.sid()
csrf = Credentials.csrf()
client = pytn.Client(username, sid_cookie=sid, csrf_cookie=csrf)

gpt_requests = 0
weather_requests = 0
translate_requests = 0
error_message = "ERROR:UNKNOWN_COMMAND. Please check spelling."
print("Running Program.")

# if a command was sent when service was
# offline, notify that user

new_messages = client.get_unread_messages()
for message in new_messages:
    message.mark_as_read()
    # message.send_sms("Service is now back online. You may now send your command.")
    # print("Notified user of service now online")

# checks for new messages, then activate the command


@client.on("message")
def handler(msg):
    if msg.type == pytn.MESSAGE_TYPE:
        message_content = msg.content
        if str(message_content[0]) == "!":
            Command_Admin.command_count += 1
            Command_Admin.valid_command_count += 1

            if str.lower(message_content) == "!weather":
                print("command activated: weather")
                asyncio.run(Command_Weather.weather_command(msg))

            elif str.lower(message_content)[:5] == "!help":
                print("command activated: help")
                asyncio.run(Command_Help.help_command(msg, message_content))

            elif str.lower(message_content) == "!details":
                print("command activated: details")
                asyncio.run(Command_Details.details_command(msg))

            elif str.lower(message_content) == "!status":
                print("command activated: status")
                asyncio.run(Command_Status.status_command(msg))

            elif str.lower(message_content) == "!secret":
                print("command activated: secret")
                asyncio.run(Command_Secret.secret_command(msg))

            elif str.lower(message_content) == "!admin":
                print("command activated: admin")
                asyncio.run(Command_Admin.admin_command(msg))

            elif str.lower(message_content) == "!gpt" or str.lower(message_content) == "!chatgpt":
                print("command activated: gpt")
                asyncio.run(Command_GPT.gpt_command(msg))

            elif str.lower(message_content) == "!qr" or str.lower(message_content) == "!qrcode":
                print("command activated: qr code")
                asyncio.run(Command_QR.qr_command(msg))

            elif str.lower(message_content) == "!translate":
                print("command activated: translate")
                asyncio.run(Command_Translate.translate_command(msg))

            elif str.lower(message_content) == "!dictionary":
                print("command activated: dictionary")
                asyncio.run(Command_Dictionary.dict_command(msg))

            elif str.lower(message_content) == "!bulletin" or str.lower(message_content) == "!news":
                print("command activated: bulletin")
                Command_bulletin.bulletin_command(msg)

            # if command is invalid

            else:
                print(f'Unknown command "{message_content}".')
                Command_Admin.valid_command_count -= 1
                msg.send_sms(error_message)

                # TODO: update readme on new release
