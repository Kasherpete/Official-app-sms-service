import pytextnow as pytn
import Credentials

# client initialization

username = Credentials.username()
sid = Credentials.sid()
csrf = Credentials.csrf()
client = pytn.Client(username, sid_cookie=sid, csrf_cookie=csrf)


async def help_command(msg, message_content):

    # if message is just "!help"

    if str.lower(message_content) == "!help":
        msg.send_sms("The current commands are: !weather, !help, !details, !status, !GPT, !qr, !translate, and !dictionary. Say !help <command> to get help on that specific command.")

    # if message is "!help <command>"

    elif str.lower(message_content) == "!help weather" or str.lower(message_content) == "!help !weather":
        msg.send_sms("The !weather command will ask your location then get the weather for you area.")

    elif str.lower(message_content) == "!help help" or str.lower(message_content) == "!help !help":
        msg.send_sms("The help command will give you instructions and details on what commands there are and how to use them.")

    elif str.lower(message_content) == "!help details" or str.lower(message_content) == "!help !details":
        msg.send_sms("The !details command will give you details on this service and its development.")

    elif str.lower(message_content) == "!help status" or str.lower(message_content) == "!help !status":
        msg.send_sms("The !status command will give you information on the different server's statuses.")

    elif str.lower(message_content) == "!help admin" or str.lower(message_content) == "!help !admin":
        msg.send_sms("The !admin command grants administrator privileges to user.")

    elif str.lower(message_content) == "!help gpt" or str.lower(message_content) == "!help chatgpt" or str.lower(message_content) == "!help !gpt" or str.lower(message_content) == "!help !chatgpt":
        msg.send_sms("The !gpt or !chatgpt command gives access to the GPT-3 network. Please use this command sparingly to keep costs down.")

    elif str.lower(message_content) == "!help gpt" or str.lower(message_content) == "!help chatgpt" or str.lower(message_content) == "!help !gpt" or str.lower(message_content) == "!help !chatgpt":
        msg.send_sms("The !qr or !qrcode generates a qr code for any website you want. Qr code scanning will be available soon.")
        # TODO: when I add qr code scanning too, update this

    elif str.lower(message_content) == "!help translate" or str.lower(message_content) == "!help !translate":
        msg.send_sms("The !translate command will translate any text into any language. It is ran off of a 3rd party google translate API to keep costs to a zero.")

    elif str.lower(message_content) == "!help dictionary" or str.lower(message_content) == "!help !dictionary":
        msg.send_sms("The !dictionary command will give you a definition on a certain word. This command is currently in development, and new features will be added soon.")

    # if command is invalid

    else:
        print('ERROR:INVALID_COMMAND. Please enter a valid command to get help on.')
        msg.send_sms("ERROR:INVALID_COMMAND. Please enter a valid command to get help on.")


