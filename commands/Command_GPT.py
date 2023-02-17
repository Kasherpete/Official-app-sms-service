import openai
import Credentials
import Custom_Message_protocols as sms
import asyncio

# client initialization

openai.api_key = Credentials.openai_key()
model_engine = "text-davinci-003"
max_tokens = 150


async def gpt_command(msg):
    user_response = await sms.ask("Input your prompt now (Character limit: 80)", msg, 60, "")
    prompt = user_response

    # checks to make sure user's input is <= 80 chars

    if len(prompt) <= 80:

        # Generate a response

        msg.send_sms("GPT-3 is generating a response, Please Wait...")
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
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
            await asyncio.sleep(1)
            print(message)
            msg.send_sms(f'GPT-3: {message}')

    # does this if prompt entered is over 80 chars

    else:
        prompt_length = len(prompt)
        msg.send_sms("ERROR: request too long. (" + str(prompt_length) + "/80 characters). Please use !gpt again to re-try")


