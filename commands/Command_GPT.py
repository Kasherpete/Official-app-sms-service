import openai
import Credentials
import Custom_Message_protocols as sms
import Main

# client initialization

openai.api_key = Credentials.openai_key()
model_engine = "text-davinci-003"
max_tokens = 450


async def gpt_command(msg):
    user_response = await sms.ask("Input your prompt now (Character limit: 200)", msg, 60, "")
    prompt = user_response

    # checks to make sure user's input is <= 80 chars

    if len(prompt) <= 200:

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
        if completion.usage["completion_tokens"] >= 420:
            sms.send_sms(f"GPT-3: {completion.choices[0].text} (GPT-3's response may be cut off due to usage limits to keep our costs down.)", msg)
        else:
            sms.send_sms(f'GPT-3: {completion.choices[0].text}', msg)

    # does this if prompt entered is over 80 chars

    else:
        prompt_length = len(prompt)
        print("ERROR: request too long. (" + str(prompt_length) + "/200 characters). Please use !gpt again to re-try")
        msg.send_sms("ERROR: request too long. (" + str(prompt_length) + "/200 characters). Please use !gpt again to re-try")


