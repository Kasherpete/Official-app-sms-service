from Custom_Message_protocols import send_sms


def bulletin_command(msg):
    send_sms("Current progress and news: Version 1.4.4 is now here! Send @gabb01 to 81010 to receive "
             "announcements for future updates. Due to a large amount of requests, the translator command may not "
             "work, so we are working on a fix for it, thank you for your patience! The prompt limit for GPT-3 is now "
             "200 compared to the previous 80, and GPT-3's response limit is now 450 compared to the previous 150 in "
             "version 1.4.43. CSS games have also been "
             "found to be able to work on the Gabb phone, "
             "so we are currently working on making a library of downloadable games for it. We are also looking "
             "into adding memes, google maps, and Discord. If you have any suggestions or bug reports, "
             "please message (629) 240-4333. We are currently looking for any ideas and possibilities for our "
             "service.", msg)
