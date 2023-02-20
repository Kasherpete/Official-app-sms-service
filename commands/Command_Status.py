import pytextnow as pytn
import Credentials
import requests

import Main

# client initialization

username = Credentials.username()
sid = Credentials.sid()
csrf = Credentials.csrf()
client = pytn.Client(username, sid_cookie=sid, csrf_cookie=csrf)


async def status_command(msg):
    msg.send_sms("Gathering Information...")

    # get server responses

    Main.weather_requests += 1
    weather_response = requests.get("http://api.openweathermap.org/data/2.5/weather?" + "appid=" + Credentials.weather_key() + "&q=" + "chicago" + "," + "IL" + "," + "US")
    openai_response = requests.get("https://status.openai.com/")

    # parse server responses

    status_list = ""

    # weather

    if weather_response.ok:
        status_list += "weather_server: ONLINE. "
    else:
        status_list += "weather_server: NO_RESPONSE. "

    # sms

    if True:
        status_list += "sms_server: ONLINE. "

    # gpt

    if openai_response.ok:
        status_list += "openAI_server: ONLINE. "
    else:
        status_list += "openAI_server: NO_RESPONSE. "

    # google translate

    if True:
        status_list += "translator: ONLINE. "

    # send off status

    msg.send_sms(status_list)

