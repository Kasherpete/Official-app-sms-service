from pytextnow import Client
import Credentials
import Custom_Message_protocols as sms
from asyncio import sleep
import openai

import Main


# some counters

command_count = 0
valid_command_count = 0

# client initialization

username = Credentials.username()
sid = Credentials.sid()
csrf = Credentials.csrf()
client = Client(username, sid_cookie=sid, csrf_cookie=csrf)


async def admin_command(msg):
    password = await sms.ask("ENTER PASSWORD", msg, 60, "")

    if password == "Eth0s2023!":

        # add anything that you want only accessible to administrators.

        print(f'user "{msg.number}" has gained access to the admin command.')
        user_response = await sms.ask("Correct password. This command is currently in development. Respond with 1 to access GPT-3 with admin permissions, and 2 for counters.", msg, 60, "")

        # if response = 1, do GPT-3 command (admin)

        if user_response == "1":
            user_response = await sms.ask("You currently have access to complete GPT-3 control. Input your prompt now (Character limit: None)", msg, 60, "")

            # set GPT-3 parameters

            openai.api_key = Credentials.openai_key()
            model_engine = "text-davinci-003"
            max_tokens = 1000

            # Generate a response

            msg.send_sms("GPT-3 is generating a response, Please Wait...")

            Main.gpt_requests += 1
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=user_response,
                max_tokens=max_tokens,
                temperature=0.5,
                top_p=0.5,
                frequency_penalty=0,
                presence_penalty=0
            )

            # break up the response into separate texts for longer responses

            if completion.usage["completion_tokens"] >= 1000:
                sms.send_sms(
                    f"GPT-3: {completion.choices[0].text} (GPT-3's response may be cut off due to usage limits to keep our costs down.)",
                    msg)
            else:
                sms.send_sms(f'GPT-3: {completion.choices[0].text}', msg)

        elif user_response == "2":
            msg.send_sms(f"Valid commands sent: {str(valid_command_count)}. Total commands sent: {str(command_count)}. Weather requests made: {str(Main.weather_requests)}. GPT-3 requests made: {str(Main.gpt_requests)}. Translate requests made: {str(Main.translate_requests)}. Note: these are measured from the start of the program.")

    # if user gets password wrong, lock

    else:
        print(f'user "{msg.number} tried to access admin and failed. user locked for one minute')
        msg.send_sms("Incorrect password. User locked for one minute.")
        await sleep(60)
