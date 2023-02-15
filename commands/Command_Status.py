import pytextnow as pytn
import Credentials
import requests

# client initialization

username = Credentials.username()
sid = Credentials.sid()
csrf = Credentials.csrf()
client = pytn.Client(username, sid_cookie=sid, csrf_cookie=csrf)


async def status_command(msg):
    msg.send_sms("Gathering Information...")

    # get server responses

    weather_response = requests.get("http://api.openweathermap.org/data/2.5/weather?" + "appid=" + Credentials.weather_key() + "&q=" + "chicago" + "," + "IL" + "," + "US")

    # parse server responses

    status_list = ""
    if weather_response.ok:
        status_list += "weather_server: OK "
    else:
        status_list += "weather_server: NoResponse"
    if True:
        status_list += "sms_server: OK "

    # send off status

    msg.send_sms(status_list)

