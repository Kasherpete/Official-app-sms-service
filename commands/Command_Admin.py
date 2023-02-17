import pytextnow as pytn
import Credentials
import Custom_Message_protocols as sms
import asyncio
import openai

# client initialization


username = Credentials.username()
sid = Credentials.sid()
csrf = Credentials.csrf()
client = pytn.Client(username, sid_cookie=sid, csrf_cookie=csrf)


async def admin_command(msg):
    password = await sms.ask("ENTER PASSWORD", msg, 60, "")

    if password == Credentials.admin_password():

        # add anything that you want only accessible to administrators.

        user_response = await sms.ask("Correct password. This command is currently in development. Respond with 1 to access GPT-3 with admin permissions.", msg, 60, "")

        # if response = 1, do GPT-3 command (admin)

        if user_response == "1":
            user_response = await sms.ask("You currently have access to complete GPT-3 control. Input your prompt now (Character limit: None)", msg, 60, "")

            # set GPT-3 parameters

            openai.api_key = Credentials.openai_key()
            model_engine = "text-davinci-003"
            max_tokens = 1000

            # Generate a response

            msg.send_sms("GPT-3 is generating a response, Please Wait...")
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

            sms_limit = 150
            gpt_response = completion.choices[0].text.replace("\n", '      ')
            gpt_response = gpt_response.replace('"', "*")
            list_response = [gpt_response[i:i + sms_limit] for i in
                             range(0, len(gpt_response), sms_limit)]

            # send the messages to user

            for message in list_response:
                msg.send_sms(f'GPT-3: {message}')
                await asyncio.sleep(1)
                print(message)

        elif user_response == 2:
            print()

    # if user gets password wrong, lock

    else:
        msg.send_sms("Incorrect password. User locked for one minute.")
        await asyncio.sleep(60)
