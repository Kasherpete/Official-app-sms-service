import openai
import Credentials
import Custom_Message_protocols as sms
import Main
import asyncio

openai.api_key = Credentials.openai_key()
model_engine = "text-davinci-003"
max_tokens = 150




async def gpt_command(msg):
    user_response = await sms.ask("Input your prompt now (Character limit: 80)", msg, 60, "")
    prompt = user_response
    if len(prompt) <= 80: #checks to make sure GPT-3's response is <= 80 chars
        # Generate a response
        sms.send("GPT-3 is generating a response, Please Wait...")
        completion = openai.Completion.create(#open ai does some black magic fuckery
            engine=model_engine,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.6,
            top_p=.5,
            frequency_penalty=0,
            presence_penalty=0
        )
    else:
        promptlength = len(prompt)
        sms.send("ERROR: request too long (" + promptlength + "/80 characters). Please use !gpt again to re-try")
    n = 150
    response = [completion.choices[0].text.replace("\n", '      ')[i:i + n] for i in range(0, len(completion.choices[0].text.replace("\n", '      ')), n)]

    for message in response:
        await asyncio.sleep(1)
        print(message)
        msg.send_sms(f'GPT-3: {message}')

