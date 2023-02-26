import requests
import Custom_Message_protocols as sms
import Credentials
import pytextnow as pytn
import json

# client initialization

username = Credentials.username()
sid = Credentials.sid()
csrf = Credentials.csrf()
client = pytn.Client(username, sid_cookie=sid, csrf_cookie=csrf)


async def qr_command(msg):
    user_response = await sms.ask("Would you like to create or read a qr code? Respond with 1 to create, and 2 to read. (Note: This will not work if you do not have an MMS subscrption.)", msg, 60, "1")
    if user_response == "1":
        await qr_generate_command(msg)
    elif user_response == "2":
        await qr_read_command(msg)


async def qr_generate_command(msg):
    user_response = await sms.ask("Input the data you would like a qr code for. (If enter a website, remember to add https:// before)", msg, 60, "https://google.com")

    # get server response

    img_data = requests.get(f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={user_response}").content

    # dump response data into loadimage.png

    with open('loadimage.png', 'wb') as handler:
        handler.write(img_data)

    file_path = "loadimage.png"
    client.send_mms(msg.number, file_path)


async def qr_read_command(msg):

    user_response = await sms.ask_advanced("Send your picture now.", msg, 60, "")

    if user_response.type == 1:  # if message is mms

        # download the file sent by user

        file = f"download.{user_response.extension}"
        user_response.mv(file)

        # http request

        url = 'http://api.qrserver.com/v1/read-qr-code/'
        myfiles = {'file': open(file, 'rb')}
        x = requests.post(url, files=myfiles)

        # parse and send response

        x = json.loads(x.text)
        x = x[0]["symbol"][0]["data"]
        sms.send_sms(x, msg)
    else:  # if message is sms
        msg.send_sms("ERROR:INVALID_TYPE. This error occurred because you did not respond with an image.")
