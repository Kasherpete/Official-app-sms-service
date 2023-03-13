# Overview
This is a project by the Eth0s group to enable certain features over sms available.

This service runs off of twilio. You will need an active phone number and your SID/auth token.
The sms service we used to use was PyTextNow, which runs off of TextNow. To get the sid, csrf, and username found in
credentials.py, ONLY FOR OLDER VERSIONS refer to [this link](https://github.com/leogomezz4t/PyTextNow_API). The newest
version uses a different python package (developed by me) that can be found
[here](https://github.com/Kasherpete/twilio-helper).
 
# Setup
### Account Setup:
You will need the following accounts and keys:  
* [Weather API](https://weatherapi.com)
* [Open Weather Map API](https://openweathermap.com/)
* [OpenAI SDK](https://openai.com)
* [Twilio SDK](https://twilio.com)
### Installation:
Run the following commands in your project terminal:

`git clone https://github.com/Kasherpete/Official-app-sms-service.git`

Or use

`gh repo clone Kasherpete/Official-app-sms-service`

To clone the project to your repository. ***If dependencies are not automatically installed, install each of them
yourself manually.***
### Setting up Credentials.py:

Copy and paste each API key to credentials.py. For example, you would paste your OpenAI key here:

```python
def openai_key():
 
    key = ""  # your key goes here
    
    return key
```
### Setting up program for specific use cases:
```python
while True:

    messages = client.get_unread_messages()  # get all unread msgs
    
    for msg in messages:  # do this for each new message received
     
        msg.send_sms("Hello World!")
        msg.mark_as_read()
            

    # how often to check for new messages. I have found this is the most stable, keep on this number if you can.
    time.sleep(.5)

```
_**I urge anyone**_ who wants to set up this program for their own personal use to check out
[This repository](https://github.com/Kasherpete/twilio-helper) for more details on the Message class and Client class
to best utilize the functionality of Twilio with the ease of other sms APIs that are best for beginners. It is
developed by myself and make everything easier for newcomers to Python.
### Running program:
Just run the program (Main.py) in your program editor, or in your terminal.

# Admin Command
You will find a command file named Command_Admin.py. This file is for use at your disposal for any of your needs,
although we may add some functionality to this command that gets uploaded to GitHub. For most use cases, changing this
command shouldn't be necessary.
# Known Limitations
### Current limitations
There are some current limitations, including the ability to handle multiple users at once (Documented
[Here](https://github.com/Kasherpete/Official-app-sms-service/issues/2)). Hopefully there will be a fix for it in the
near future
### Previous limitations
**_Below version 1.7 beta 1_**, There were a few "bugs" that were present, mainly due to PyTextNow version 1.1.9 that
make it not possible to send certain characters. This includes quotation marks and the reverse backslash (so you cannot
use \n). The program deals with this by inserting multiple spaces instead of \n, and * instead of ", although this has
been changed since implementing twilio.
# Versions and Updates
1.7.4 - Fixed multiple features, optimizations, overall added "neatness". Also added really cool "admin portal".

1.7.3 - Added usage limit for each number. Limit 15 per day. Bypassed by saying !add and entering correct password.

1.7.2 - Added weather features

1.7.1 - Every command now works. The code is now officially TextNow independent, and is being run completely off of
Twilio.

1.7 Beta Release 5 - bug, performance fixes/optimizations

1.7 Beta Release 4 - All commands functional with the exception of !qr. Improved ChatGPT experience as well as bug
fixes, documentation, error handling, and minor added features.

1.7 beta 3 - Most commands seem to now work except for !qr.

1.7 beta 1 - Utilizes the twilio helper (https://github.com/Kasherpete/twilio-helper) to start porting over to using
twilio. It is almost completely dysfunctional as far as the commands go.

1.4.52 - Bug fixes, more spam prevention.

1.4.5 - Added bug fixes that make service look like spam. Weather responses are put in one single message and when
long texts are broken up, they now get sent at an interval of four.

1.4.43 - Minor updates to admin, bulletin, gpt, translate commands and added error correction.

1.4.4 - Updated dictionary command.

1.4.38 - Added qr code reader in addition to the already existing qr code generator.

1.4.32 - Added bulletin command to inform users of progress on the service.

1.4.31 - Added dictionary command. This is still a beta, so more features will be added in the near future.

1.4.2 - Added translate command.

1.4.1 - Added qr code generator. Plans in place to add qr code reader.

1.4.0  -  Updated admin command, added some counters available to administrators, added a function that when a user 
tries to send command when service is offline, the program sends a notification to the user on start that signals its
now online status.

