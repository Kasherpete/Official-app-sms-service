from googletrans import Translator
import googletrans.constants
import Custom_Message_protocols as sms
import asyncio

import Main


async def translate_command(msg):

    user_response = await sms.ask("Input the two letter language abbreviation your text is in. (For a list of abbreviations, say help.)", msg, 60, "en")
    if str.lower(user_response) == "help":
        lang = str(googletrans.constants.LANGUAGES)
        sms_limit = 150
        list_response = [lang[i:i + sms_limit] for i in
                         range(0, len(lang), sms_limit)]

        for message in list_response:

            # I know this is a long wait, but the phone cannot
            # handle so many texts, and it crashes the phone.

            await asyncio.sleep(3)
            msg.send_sms(message)
    else:
        translator = Translator()
        lang1 = str.lower(user_response)
        user_response = await sms.ask("Input the two letter language abbreviation you want your text in.", msg, 60, "es")
        lang2 = str.lower(user_response)
        user_response = await sms.ask("Input your text now.", msg, 60, "Hello.")
        text = user_response
        try:
            Main.translate_requests += 1
            new_text = translator.translate(text, dest=lang2, src=lang1)
            print(new_text.text)
            msg.send_sms(new_text.text)
        except ValueError:
            msg.send_sms("ERROR:TRANSLATE_ERROR. This error may be caused by inputting an invalid value. Please run the command again to retry.")