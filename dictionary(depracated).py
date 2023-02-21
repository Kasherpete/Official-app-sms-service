import PyDictionary
import asyncio
import Custom_Message_protocols as sms


async def dictionary(msg):

    user_response = await sms.ask("If you want the meaning a the word, respond with 1. If you want synonyms a the word, repond with 2.", msg, 60, "1")
    dictionary = PyDictionary.PyDictionary()

    if user_response == "1":

        user_response = await sms.ask("Input your word now.", msg, 60, "")
        response = dictionary.meaning(user_response)
        sms.send_sms(str(response), msg)

    #

    elif user_response == "2":
        user_response = await sms.ask("Input your word now.", msg, 60, "")
        response = dictionary.synonym(user_response)
        sms.send_sms(str(response), msg)

# space and jopes, this code right here:
# response = dictionary.meaning(user_response)
# takes a long time to execute, and i unfortunately
# cannot make it async. also, the synonym function
# doesn't really seem to work :p
