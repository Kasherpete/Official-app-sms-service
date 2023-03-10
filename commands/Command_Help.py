

async def help_command(msg, message_content):

    # if message is just "!help"

    if str.lower(message_content) == "!help":
        msg.send_sms("The current commands are: !weather, !help, !details, !bulletin, !status, !GPT, !qr, !translate, !dictionary, !add, and !test. Say !help <command> to get help on that specific command, like !help weather or !help status. Also, if you have not already, send @gabb01 to 81010 to sign up to receive announcements for future updates.")

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

    elif str.lower(message_content) == "!help qr" or str.lower(message_content) == "!help !qr" or str.lower(message_content) == "!help qrcode" or str.lower(message_content) == "!help !qrcode":
        msg.send_sms("The !qr or !qrcode generates or reads a qr code for any website you want.")

    elif str.lower(message_content) == "!help translate" or str.lower(message_content) == "!help !translate":
        msg.send_sms("The !translate command will translate any text into any language. It is ran off of a 3rd party google translate API to keep costs to a zero.")

    elif str.lower(message_content) == "!help dictionary" or str.lower(message_content) == "!help !dictionary":
        msg.send_sms("The !dictionary command will give you a definition(s) on a certain word. You can also now use it as a thesaurus as of version 1.4.4.")

    elif str.lower(message_content) == "!help bulletin" or str.lower(message_content) == "!help !bulletin" or str.lower(message_content) == "!help news" or str.lower(message_content) == "!help !news":
        msg.send_sms("The !bulletin command will inform you on any development currently being made on this service. You can also say !news.")

    elif str.lower(message_content) == "!help add" or str.lower(message_content) == "!help !add":
        msg.send_sms("The !add command will add you to a list of Premium users. You can only be added if you are a Patreon Supporter.")

    elif str.lower(message_content) == "!help test" or str.lower(message_content) == "!help !test":
        msg.send_sms("The !test command checks to see if you are in the list of Premium Members. This command is mainly for bug testing purposes.")

    # if command is invalid

    else:
        print('ERROR:INVALID_COMMAND. Please enter a valid command to get help on.')
        msg.send_sms("ERROR:INVALID_COMMAND. Please enter a valid command to get help on.")


