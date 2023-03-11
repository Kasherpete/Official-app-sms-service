import Custom_Message_protocols as sms
from asyncio import sleep
# import openai
import Main
from . import Command_Patron


# some counters



# client initialization




async def admin_command(msg):
    password = await sms.ask("ENTER PASSWORD", msg, 60, "")

    if password == "Eth0s2023!":

        # add anything that you want only accessible to administrators.

        print(f'user "{msg.number}" has gained access to the admin command.')
        user_response = await sms.ask("Correct password. This command is currently in development. Respond with 1 to access ChatGPT with admin permissions, 2 for counters, or 3 for program control access.", msg, 60, "")

        # if response = 1, do GPT-3 command (admin)

        if user_response == "1":
            # going to add some ChatGPT admin perms soon
            msg.send_sms("Just use the !gpt command, it does the same thing")

        elif user_response == "2":
            msg.send_sms(f"Valid commands sent: {str(Main.valid_command_count)}. Total commands sent: {str(Main.command_count)}. Weather requests made: {str(Main.weather_requests)}. GPT-3 requests made: {str(Main.gpt_requests)}. Translate requests made: {str(Main.translate_requests)}. Note: these are measured from the start of the program.")

        elif user_response == "3":
            user_response = await sms.ask("Input 1 to terminate program, and 2 for patron member accesses.", msg, 60, 0)

            if user_response == "1":
                user_response = await sms.ask("Are you sure? Respond yes or no. Only do this if it is absolutely necessary.", msg, 60, "no")

                if str.lower(user_response) == "yes":
                    msg.send_sms("Process terminating...")
                    msg.send_sms("Process finished with exit code 0")
                    quit()

                elif str.lower(user_response) == "no":
                    msg.send_sms("Canceled.")

                else:
                    msg.send_sms("Incorrect response.")

            elif user_response == "2":
                if Command_Patron.patron_list:
                    msg.send_sms(Command_Patron.patron_list)
                else:
                    msg.send_sms("No enrolled members.")

            else:
                msg.send_sms("Incorrect response.")

        else:
            msg.send_sms("Incorrect response.")
    # if user gets password wrong, lock

    else:
        print(f'user "{msg.number} tried to access admin and failed. user locked for one minute')
        msg.send_sms("Incorrect password. User locked for one minute.")
        await sleep(60)
