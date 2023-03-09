import Custom_Message_protocols as sms
from asyncio import sleep
# import openai

import Main


# some counters

command_count = 0
valid_command_count = 0

# client initialization




async def admin_command(msg):
    password = await sms.ask("ENTER PASSWORD", msg, 60, "")

    if password == "Eth0s2023!":

        # add anything that you want only accessible to administrators.

        print(f'user "{msg.number}" has gained access to the admin command.')
        user_response = await sms.ask("Correct password. This command is currently in development. Respond with 1 to access ChatGPT with admin permissions, and 2 for counters.", msg, 60, "")

        # if response = 1, do GPT-3 command (admin)

        if user_response == "1":
            # going to add some ChatGPT admin perms soon
            msg.send_sms("Just use the !gpt command, it does the same thing")

        elif user_response == "2":
            msg.send_sms(f"Valid commands sent: {str(valid_command_count)}. Total commands sent: {str(command_count)}. Weather requests made: {str(Main.weather_requests)}. GPT-3 requests made: {str(Main.gpt_requests)}. Translate requests made: {str(Main.translate_requests)}. Note: these are measured from the start of the program.")

    # if user gets password wrong, lock

    else:
        print(f'user "{msg.number} tried to access admin and failed. user locked for one minute')
        msg.send_sms("Incorrect password. User locked for one minute.")
        await sleep(60)
