import requests
import json
import Credentials
import Custom_Message_protocols as sms
from asyncio import sleep
from math import floor
import Main

# client initialization




async def v1weather(msg):

    # local initialization

    country_code = "US"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # get the city and state from user

    resp = await sms.ask("Input city name:", msg, 60, "Chicago")

    city_name = resp
    resp = await sms.ask("Input two letter state abbreviation:", msg, 60, "IL")

    state_code = resp

    # get the weather data

    complete_url = base_url + "appid=" + Credentials.open_weather_key() + "&q=" + city_name + "," + state_code + "," + country_code
    Main.weather_requests += 1
    response = requests.get(complete_url)

    # parse the data

    request_response = response.json()
    if request_response["cod"] != "404" and request_response["cod"] != "400":

        # assign api response to variables

        request_response_main = request_response["main"]

        current_temperature = (request_response_main["temp"]*1.8 - 459.67)
        current_temperature = floor(current_temperature)
        current_pressure = request_response_main["pressure"]
        current_humidity = request_response_main["humidity"]
        z = request_response["weather"]
        weather_description = z[0]["description"]

        # return data to the user
        msg.send_sms(f"Weather in {str(city_name)}, {str(state_code)}:\n{str(weather_description)}.\nTemp: {str(current_temperature)}\u00B0\u0046.\nAir pressure: {current_pressure}hpa.\nHumidity: {str(current_humidity)}%.")


    else:
        error1 = "ERROR:WEATHER_NO_RESPONSE. Please check that you entered the correct city, or say !status to check " \
                 "the weather server's status."
        msg.send_sms(error1)








async def v2weather(msg):
    try:

        # ask user for current weather, forecast, or advanced

        Main.weather_requests += 1
        user_response = await sms.ask("Respond with 1 for current weather, 2 for forecast, and 3 for advanced weather queries:", msg, 60, "1")


        if user_response == "3":

            # ask next question

            user_response = await sms.ask("Respond with 1 for detailed current weather, 2 for detailed forecast, 3 for radar in the US, and 4 for custom radar station areas:", msg, 60, "1")

            # radar

            if user_response == "3":
                # msg.send_sms("This feature is currently in development.")
                msg.send_mms("", "https://radar.weather.gov/ridge/standard/CONUS_loop.gif")
            elif user_response == "4":
                # msg.send_sms("This feature is currently in development.")
                user_response = await sms.ask("enter radar station name.", msg, 60, "CONUS")
                msg.send_mms("", "https://radar.weather.gov/ridge/standard/" + str.upper(user_response) + "_loop.gif")


            # forecast

            elif user_response == "2":

                # advanced forecast

                user_response = await sms.ask("Respond with 1 to get detailed forecast over text. Respond with 2 to get hourly forecast for a specific day (will send a lot of texts):", msg, 60, "1")

                if user_response == "1":


                    area = await sms.ask("Input city name:", msg, 60, "Chicago")
                    area += f", {await sms.ask('Input state:', msg, 60, 'Il')}"
                    try:
                        days = int(await sms.ask("Input how many days of forecast you would like, 1-10:", msg, 60, "3"))
                        if days >= 10:
                            days = 1
                    except ValueError:
                        msg.send_sms("Error, Please enter a valid response.")
                        days = 1
                    r = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={Credentials.weatherapi_key()}&q={area}&days={days}&aqi=no&alerts=no")
                    r = json.loads(r.text)
                    try:
                        r = r["forecast"]["forecastday"]
                        for day in range(days):
                            msg.send_sms(
                                f"{r[day]['date']} forecast: {r[day]['day']['condition']['text']}\nMaxTemp: {r[day]['day']['maxtemp_f']}F\nMinTemp: {r[day]['day']['mintemp_f']}F\nAvgTemp: {r[day]['day']['avgtemp_f']}F\nMaxWind: {r[day]['day']['maxwind_mph']}mph\nHumidity: {int(r[day]['day']['avghumidity'])}%\nTotalPrecip: {int(r[day]['day']['totalprecip_in'])}in.\nChanceOfRain: {r[day]['day']['daily_chance_of_rain']}%\nAvgVis: {int(r[day]['day']['avgvis_miles'])}miles\nCode {r[day]['day']['condition']['code']}.")
                            await sleep(4)
                    except KeyError:
                        msg.send_sms("Error, Please enter a valid city and state name.")


                elif user_response == "2":

                    days = int(await sms.ask("Which day relative from now do you want to get the weather for? 1-10 (say 5 to get the weather for 5 days from now):", msg, 60, "3"))

                    area = await sms.ask("Input city name:", msg, 60, "Chicago")
                    area += f", {await sms.ask('Input state:', msg, 60, 'Il')}"
                    r = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={Credentials.weatherapi_key()}&q={area}&days={days+1}&aqi=no&alerts=no")
                    r = json.loads(r.text)
                    r = r["forecast"]["forecastday"]
                    for i in range(8):
                        i *= 3
                        msg.send_sms(f"Hour {i} of day {r[days]['date']}: {r[days]['hour'][i]['condition']['text']}\nTemp: {r[days]['hour'][i]['temp_f']}F\nWind: {r[days]['hour'][i]['wind_mph']}mph\nWindDir: {r[days]['hour'][i]['wind_dir']}\nPressure: {r[days]['hour'][i]['pressure_in']}in\nHumidity: {r[days]['hour'][i]['humidity']}%\nCloudCover: {r[days]['hour'][i]['cloud']}%")
                        await sleep(4)

                else:
                    msg.send_sms("Error, Please enter a valid response.")

            elif user_response == "1":

                # detailed current weather

                area = await sms.ask("Input city name:", msg, 60, "Chicago")
                area += f", {await sms.ask('Input state:', msg, 60, 'Il')}"
                r = requests.get(f"http://api.weatherapi.com/v1/current.json?key={Credentials.weatherapi_key()}&q={area}&aqi=no")
                r = json.loads(r.text)
                msg.send_sms(
                    f"Weather in {r['location']['name']}, {r['location']['region']}: {r['current']['condition']['text']}\nTemp: {int(r['current']['temp_f'])}F\nWind: {int(r['current']['wind_mph'])}mph\nWindGust: {int(r['current']['gust_mph'])}mph\nWindDirection: {r['current']['wind_dir']}, {r['current']['wind_degree']}\nPressure: {r['current']['pressure_in']}in\nHumidity: {r['current']['humidity']}%\nCloudCover: {r['current']['cloud']}%\nLat {r['location']['lat']} Lon {r['location']['lon']}{r['current']['condition']['code']}")

            else:
                # if invalid response
                msg.send_sms("Error, Please enter a valid response.")

        # classic forecast

        elif user_response == "2":


            area = await sms.ask("Input city name:", msg, 60, "Chicago")
            area += f", {await sms.ask('Input state:', msg, 60, 'Il')}"
            try:
                days = int(await sms.ask("Input how many days of forecast you would like, 1-10:", msg, 60, "3"))
                if days >= 11:
                    days = 1
            except ValueError:
                msg.send_sms("Error, Please enter a valid response.")
                days = 1
            r = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={Credentials.weatherapi_key()}&q={area}&days={days}&aqi=no&alerts=no")
            r = json.loads(r.text)
            try:
                r = r["forecast"]["forecastday"]
                for day in range(days):
                    msg.send_sms(f"{r[day]['date']} forecast: {r[day]['day']['condition']['text']}\nMaxTemp: {r[day]['day']['maxtemp_f']}F\nMinTemp: {r[day]['day']['mintemp_f']}F\nMaxWind: {r[day]['day']['maxwind_mph']}mph\nHumidity: {int(r[day]['day']['avghumidity'])}%\nChanceOfRain: {r[day]['day']['daily_chance_of_rain']}%")
                    await sleep(4)
            except KeyError:
                msg.send_sms("Error, Please enter a valid city and state name.")

        # classic current weather

        elif user_response == "1":

            area = await sms.ask("Input city name:", msg, 60, "Chicago")
            area += f", {await sms.ask('Input state:', msg, 60, 'Il')}"
            r = requests.get(f"https://api.weatherapi.com/v1/current.json?key={Credentials.weatherapi_key()}&q={area}&aqi=no")
            r = json.loads(r.text)
            msg.send_sms(f"Weather in {r['location']['name']}, {r['location']['region']}: {r['current']['condition']['text']}\nTemp: {int(r['current']['temp_f'])}F\nWind: {int(r['current']['wind_mph'])}mph\nPressure: {r['current']['pressure_in']}in\nHumidity: {r['current']['humidity']}%\nCloudCover: {r['current']['cloud']}%")

        else:
            msg.send_sms("Error, Please enter a valid response.")


    # errors

    except KeyError:
        r = requests.get(f"http://api.weatherapi.com/v1/current.json?key={Credentials.weatherapi_key()}&q=Chicago, Il&aqi=no")
        r = json.loads(r.text)
        print(r)

        # if api key invalid

        if r["error"]['code'] == 2008:
            msg.send_sms("A fatal error has occurred, notify @Kasherpete#2661 immediately.")

        else:
            msg.send_sms("An unknown error has occurred. Notify @Kasherpete")

        # other detailed errors that are discovered will go here

    except ValueError:
        msg.send_sms("An unknown error has occurred. Notify @Kasherpete")

        # other detailed errors that are discovered will also go here

    # other errors go here

