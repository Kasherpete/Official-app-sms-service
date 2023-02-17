import pytextnow as pytn
import requests.exceptions

import Credentials
import asyncio
from commands import Command_Details, Command_Secret, Command_Status, Command_Weather, Command_Help, Command_Admin, Command_GPT

# client initialization

username = Credentials.username()
sid = Credentials.sid()
csrf = Credentials.csrf()
client = pytn.Client(username, sid_cookie=sid, csrf_cookie=csrf)
command_count = 0


error_message = "ERROR:UNKNOWN_COMMAND. Please check spelling."
print("Running Program.")


@client.on("message")
def handler(msg):
    if msg.type == pytn.MESSAGE_TYPE:
        message_content = msg.content
        if str(message_content[0]) == "!":

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

            # if command is invalid

            else:
                print(f'Unknown command "{message_content}".')
                msg.send_sms(error_message)
        

