import math
import requests
import Credentials
import Custom_Message_protocols as sms
import Main

# client initialization




async def weather_command(msg):

    # local initialization

    city_name = "chicago"
    state_code = "il"
    country_code = "us"
    api_key = Credentials.weather_key()
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # get the city and state from user

    resp = await sms.ask("Input city name:", msg, 60, "Chicago")
    if resp != "" and resp is not None:
        city_name = resp
    resp = await sms.ask("Input two letter state abbreviation:", msg, 60, "IL")
    if resp != "" and resp is not None:
        state_code = resp

    # get the weather data

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "," + state_code + "," + country_code
    Main.weather_requests += 1
    response = requests.get(complete_url)

    # parse the data

    request_response = response.json()
    if request_response["cod"] != "404" and request_response["cod"] != "400":

        # assign api response to variables

        request_response_main = request_response["main"]

        current_temperature = (request_response_main["temp"]*1.8 - 459.67)
        current_temperature = math.floor(current_temperature)
        current_pressure = request_response_main["pressure"]
        current_humidity = request_response_main["humidity"]
        z = request_response["weather"]
        weather_description = z[0]["description"]

        # return data to the user
        msg.send_sms(f"Weather in {str(city_name)}, {str(state_code)}:\n{str(weather_description)}.\nTemp: {str(current_temperature)}\u00B0\u0046.\nAir pressure: {current_pressure}hpa.\nHumidity: {str(current_humidity)}%.")


    else:
        error1 = "ERROR:WEATHER_NO_RESPONSE. Please check that you entered the correct city, or say !status to check " \
                 "the weather server's status."

