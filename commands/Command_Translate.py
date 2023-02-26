import httpcore
from googletrans import Translator
import googletrans.constants
import Custom_Message_protocols as sms
import Main


async def translate_command(msg):

    user_response = await sms.ask("Input the two letter language abbreviation your text is in. (For a list of abbreviations, say help.)", msg, 60, "en")
    if str.lower(user_response) == "help":
        lang = str(googletrans.constants.LANGUAGES)
        sms.send_sms(lang, msg)
    else:

        # asks the user for languages and prompt

        translator = Translator()
        lang1 = str.lower(user_response)
        user_response = await sms.ask("Input the two letter language abbreviation you want your text in.", msg, 60, "es")
        lang2 = str.lower(user_response)
        user_response = await sms.ask("Input your text now.", msg, 60, "Hello.")
        text = user_response

        # google translate req

        try:
            Main.translate_requests += 1
            new_text = translator.translate(text, dest=lang2, src=lang1)
            new_text = new_text.text

            # send msgs
            sms.send_sms(new_text, msg)
        except httpcore._exceptions.ReadTimeout:
            msg.send_sms("Sorry, the server was unable to complete the request. This is due to a large volume of "
                         "requests at this time. This is a known error, and is being actively worked on. Thank you "
                         "for your patience!")


