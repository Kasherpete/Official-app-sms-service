from Custom_Message_protocols import send_sms


def bulletin_command(msg):
    send_sms("Current progress and news: The service is now back online, but this time powered by Twilio! There have "
             "been a lot of under-the-hood changes in the most recent update, most notably less choppy texts and an "
             "improved ChatGPT experience. There is also now a limit to 15 commands per day, which can be bypassed by supporting us on Patreon! CSS games have also been found to be able to work on the Gabb phone, "
             "so we are currently working on making a library of downloadable games for it. We are also looking "
             "into adding memes, google maps, and Discord. If you have any suggestions or bug reports, "
             "please message (629) 240-4333. We are currently looking for any ideas and possibilities for our "
             "service.", msg)
