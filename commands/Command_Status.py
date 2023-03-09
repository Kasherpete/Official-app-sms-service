import requests
from Credentials import weather_key
import Main


async def status_command(msg):
    msg.send_sms("Gathering Information...")

    # get server responses

    Main.weather_requests += 1
    weather_response = requests.get("http://api.openweathermap.org/data/2.5/weather?" + "appid=" + weather_key() + "&q=" + "chicago" + "," + "IL" + "," + "US")
    openai_response = requests.get("https://status.openai.com/")
    dictionary_response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/word")

    # parse server responses

    status_list = ""

    # weather

    if weather_response.ok:
        status_list += "weather_server: ONLINE.\n"
    else:
        status_list += "weather_server: NO_RESPONSE.\n"

    # sms

    if True:
        status_list += "sms_server: ONLINE.\n"

    # gpt

    if openai_response.ok:
        status_list += "openAI_server: ONLINE.\n"
    else:
        status_list += "openAI_server: NO_RESPONSE.\n"

    # google translate

    if True:
        status_list += "translator: ONLINE.\n"

    # dictionary

    if dictionary_response.ok:
        status_list += "dictionary_server: ONLINE.\n"
    else:
        status_list += "dictionary_server: NO_RESPONSE.\n"

    # send off status

    msg.send_sms(status_list)

