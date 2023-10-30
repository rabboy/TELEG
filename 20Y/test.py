import schedule
import telebot
from threading import Thread
from time import sleep

TOKEN = '5867934782:AAGrVyjbSHI7Zxzdiaeuc-5ooyO7e-jy1kw' 

bot = telebot.TeleBot(TOKEN)
some_id = 441680952 

def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)

def function_to_run():
    return bot.send_message(some_id, "This is a message to send.")

if __name__ == "__main__":
    # Create the job in schedule.
    schedule.every().saturday.at("13:03").do(function_to_run)

    # Spin up a thread to run the schedule check so it doesn't block your bot.
    # This will take the function schedule_checker which will check every second
    # to see if the scheduled job needs to be ran.
    Thread(target=schedule_checker).start() 

    # And then of course, start your server.
    bot.polling()