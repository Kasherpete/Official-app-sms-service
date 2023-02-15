import pytextnow as pytn

import Credentials
import asyncio
from commands import Command_Details, Command_Secret, Command_Status, Command_Weather, Command_Help, Command_Admin

# client initialization

username = Credentials.username()
sid = Credentials.sid()
csrf = Credentials.csrf()
client = pytn.Client(username, sid_cookie=sid, csrf_cookie=csrf)
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
            elif message_content == "!help" or message_content == "!Help":
                print("command activated: help")
                asyncio.run(Command_Help.help_command(msg))
            elif message_content == "!details" or message_content == "!Details":
                print("command activated: details")
                asyncio.run(Command_Details.details_command(msg))
            elif message_content == "!status" or message_content == "!Status":
                print("command activated: status")
                asyncio.run(Command_Status.status_command(msg))
            elif message_content == "!secret" or message_content == "!Secret":
                print("command activated: secret")
                asyncio.run(Command_Secret.secret_command(msg))
            elif message_content == "!admin" or message_content == "!Admin":
                print("command activated: admin")
                asyncio.run(Command_Admin.admin_command(msg))
            else:
                print(f'Unkown command "{message_content}". (interpreted as "{str.lower(message_content)}").')
                msg.send_sms(error_message)
        

