from httpcore import _exceptions
from googletrans import Translator
import googletrans.constants
import Custom_Message_protocols as sms
import Main


async def translate_command(msg):

    # gets lang text is in

    user_response = await sms.ask("Input the two letter language abbreviation your text is in. (For a list of "
                                  "abbreviations, say #help.)", msg, 60, "en")
    # if user responded with #help
    if str.lower(user_response) == "#help":
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

        # google translate request

        try:

            # translate magic

            Main.translate_requests += 1
            new_text = translator.translate(text, dest=lang2, src=lang1)
            new_text = new_text.text

            # send msgs

            sms.send_sms(f"Translation: {new_text}", msg)

        except _exceptions.ReadTimeout:
            msg.send_sms("Sorry, the server was unable to complete the request. This is due to a large volume of "
                         "requests at this time. This is a known error, and is being actively worked on. Thank you "
                         "for your patience!")
        except ValueError:
            msg.send_sms("You sent an invalid language abbreviation. Send the command again and say !help to get the "
                         "full list of abbreviations")


