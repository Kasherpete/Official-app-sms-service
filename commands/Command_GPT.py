import openai
import Credentials
import Custom_Message_protocols as sms
import asyncio
import Main
import pytextnow

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
        Main.gpt_requests += 1
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

        sms.send_sms(f'GPT-3: {completion.choices[0].text}', msg)

    # does this if prompt entered is over 80 chars

    else:
        prompt_length = len(prompt)
        print("ERROR: request too long. (" + str(prompt_length) + "/80 characters). Please use !gpt again to re-try")
        msg.send_sms("ERROR: request too long. (" + str(prompt_length) + "/80 characters). Please use !gpt again to re-try")


