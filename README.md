# Details
 This is a project by the Eth0s group to enable certain features over sms available.
 
 The sms service we use is PyTextNow, which runs off of textnow. To get the sid, csrf, and username found in
 credentials.py, refer to https://github.com/leogomezz4t/PyTextNow_API .
 
# Setup
 You will need a openweathermap account and key, openAI account and key, and a TextNow account. As for the dependencies,
 they can be found in requirements.txt. If you have any problems with importing modules, got to the link above to 
 install any other requirements.
 
Run these commands:

    pip install pytextnow
    pip install openai
    pip install requests

if PyTextNow does not work or an incorrect version installs, use

    git clone https://github.com/leogomezz4t/PyTextNow_API.git
 # Admin Command
 You will find a command file named Command_Admin.py. This file is for use at your disposal for any of your needs,
 although we may add some functionality to this command that gets uploaded to github.
 # Known Limitations
 There are a few "bugs" that are present, mainly due to PyTextNow version 1.1.9 that make it not possible to send 
 certain characters. This includes quotation marks and the reverse backslash (so you cannot use \n). The program deals 
 with this by inserting multiple spaces instead of \n, and * instead of ".