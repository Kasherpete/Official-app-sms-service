import json
import requests
import Custom_Message_protocols as sms


async def dict_command(msg):
    user_response_number = await sms.ask("Respond with 1 for basic definitions, 2 for synonyms and alike words, and 3 for advanced meanings and definitions.", msg, 60, "1")
    user_response = await sms.ask("Input your word now.", msg, 60, "hello")

    if user_response_number == "1":
        dict_basic(msg, user_response)
    elif user_response_number == "2":
        dict_synonym(msg, user_response)
    elif user_response_number == "3":
        dict_advanced(msg, user_response)


def dict_basic(msg, user_response):

    # request definition

    r = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{user_response}")
    completion = ""
    r = json.loads(r.text)

    # parse data

    try:
        # parse
        r = r[0]
        r = r["meanings"]
        for meaning in r:  # how many meanings

            completion += f'{meaning["partOfSpeech"]}: '
            completion += f'{meaning["definitions"][0]["definition"]} '

        # send message

        sms.send_sms(completion, msg)

    except KeyError:
        msg.send_sms("ERROR:INVALID_REQUEST. This error will be caused because of an incorrectly spelled word.")


def dict_synonym(msg, user_response):

    # make request

    r = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{user_response}")
    completion = "synonyms: "
    r = json.loads(r.text)

    # parse data

    try:
        # parse
        r = r[0]
        r = r["meanings"]
        for meaning in r:  # how many meanings
            new = meaning["synonyms"]
            for definition in new:
                completion += f"{definition}, "

        # send message

        sms.send_sms(completion, msg)

    except KeyError:
        msg.send_sms("ERROR:INVALID_REQUEST. This error will be caused because of an incorrectly spelled word.")


def dict_advanced(msg, user_response):

    # request

    r = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{user_response}")
    completion = ""
    completion += "Definitions: "
    r = json.loads(r.text)

    # parse

    try:
        # parse
        r = r[0]
        r = r["meanings"]
        for meaning in r:  # how many meanings
            new = meaning["definitions"]
            for definition in new:
                completion += f'{definition["definition"]}, '

        # send message

        sms.send_sms(completion, msg)

    except KeyError:
        msg.send_sms("ERROR:INVALID_REQUEST. This error will be caused because of an incorrectly spelled word.")
