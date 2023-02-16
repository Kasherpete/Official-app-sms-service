import openai
import Credentials
import Custom_Message_protocols as sms
import Main

openai.api_key = Credentials.openai_key()
model_engine = "text-davinci-003"
max_tokens = 255


async def chatgpt_command(msg):
    user_response = await sms.ask("Input your prompt now. Note: the maximum word length is approximately 200 words to keep costs down. You have one minute to enter your prompt to ChatGPT before timeout. Also keep in mind that it may take a minute for ChatGPT's response to generate.", msg, 60, "")
    prompt = user_response
    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    msg.send_sms(completion.choices[0].text.replace("\n", ' (newline) '))
