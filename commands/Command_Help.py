import pytextnow as pytn
import Credentials

# client initialization

username = Credentials.username()
sid = Credentials.sid()
csrf = Credentials.csrf()
client = pytn.Client(username, sid_cookie=sid, csrf_cookie=csrf)


async def help_command(msg, message_content):
    if str.lower(message_content) == "!help":
        msg.send_sms("The current commands are: !weather, !help, !details, !status, and !GPT. Say !help <command> to get help on that specific command.")
    elif str.lower(message_content) == "!help weather":
        msg.send_sms("The !weather command will get the weather for you area.")
    elif str.lower(message_content) == "!help help":
        msg.send_sms("The help command will give you instructions on how to use the commands.")
    elif str.lower(message_content) == "!help details":
        msg.send_sms("The !details command will give you details on this service.")
    elif str.lower(message_content) == "!help status":
        msg.send_sms("The !status command will give you information on the different server's statuses.")
    elif str.lower(message_content) == "!help secret":
        msg.send_sms("")
    elif str.lower(message_content) == "!help admin":
        msg.send_sms("The !admin command grants administrator privileges to user.")
    elif str.lower(message_content) == "!help gpt" or str.lower(message_content) == "!help chatgpt":
        msg.send_sms("The !gpt or !chatgpt command gives access to the GPT-3 network. Please use this command sparingly to keep costs down.")
    else:
        print(f'Unknown command "{message_content}". (interpreted as "{str.lower(message_content)}").')
        msg.send_sms("ERROR:INVALID_COMMAND. Please enter a valid command to get help on.")


