import requests
import Custom_Message_protocols as sms
import Credentials
import pytextnow as pytn

# client initialization

username = Credentials.username()
sid = Credentials.sid()
csrf = Credentials.csrf()
client = pytn.Client(username, sid_cookie=sid, csrf_cookie=csrf)


async def qr_command(msg):
    user_response = await sms.ask("Input the data you would like a qr code for. (If enter a website, remember to add https:// before)", msg, 60, "")

    # get server response

    img_data = requests.get(f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={user_response}").content

    # dump response data into loadimage.png

    with open('loadimage.png', 'wb') as handler:
        handler.write(img_data)

    file_path = "loadimage.png"
    client.send_mms(msg.number, file_path)
