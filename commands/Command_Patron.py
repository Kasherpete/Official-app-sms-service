import Custom_Message_protocols as sms
from Credentials import patreon_password

patron_list = []
msg_json = {}


async def add_patron(msg):

    user_response = await sms.ask("Enter the password you have been given. If you do not have the password, ask @Kasherpete#2661 on discord or message him on Patreon.", msg, 60, "")

    if str.lower(user_response) == patreon_password():

        if msg.number not in patron_list:
            patron_list.append(msg.number)
            msg.send_sms("Success! You have been added to the list of Premium Members.")

        else:
            msg.send_sms("You are already in the list of Premium Members.")

    else:
        msg.send_sms("Incorrect password.")

