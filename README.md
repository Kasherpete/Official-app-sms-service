# Details
 This is a project by the Eth0s group to enable certain features over sms available.
 
 This service runs off of twilio. You will need an active phone number and your SID/auth token.
 The sms service we used to use was PyTextNow, which runs off of textnow. To get the sid, csrf, and username found in
 credentials.py, ONLY FOR OLDER VERSIONS refer to https://github.com/leogomezz4t/PyTextNow_API.
 
# Setup
 You will need a openweathermap account and key, openAI account and key, and a Twilio account/phone number. As for the dependencies,
 they can be found in requirements.txt. If you have any problems with importing modules, got to the link above to 
 install any other requirements.


 # Admin Command
 You will find a command file named Command_Admin.py. This file is for use at your disposal for any of your needs,
 although we may add some functionality to this command that gets uploaded to github.
 # Known Limitations
 Below version 1.7 beta 1, There were a few "bugs" that were present, mainly due to PyTextNow version 1.1.9 that make it not possible to send 
 certain characters. This includes quotation marks and the reverse backslash (so you cannot use \n). The program deals 
 with this by inserting multiple spaces instead of \n, and * instead of ", although this will be changed after implementing
 twilio.
 # Versions and Updates
 1.7.1 - Every command now works. The code is now officially TextNow independent, and is being run completely off of Twilio.

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

