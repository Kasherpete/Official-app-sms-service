import requests
import json
import Custom_Message_protocols as sms


async def dictionary(msg):
    user_response = await sms.ask("Input your word:", msg, 60, "hello")
    r = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{user_response}")

    # parse data :p

    try:
        r = json.loads(r.text)
        r = r[0]
        r = r["meanings"]
        r = r[0]
        print(r)
        r = r["definitions"]
        print(r)
        r = r[0]
        print(r)
        r = r["definition"]
        print(r)
        sms.send_sms(r, msg)
    except KeyError:
        msg.send_sms("ERROR:ERROR_PARSING_DATA. This could be caused by inputting an incorrect word. Please run the command again to retry.")

