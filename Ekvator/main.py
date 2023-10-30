import telebot

Task =''
API_KEY = '6585853521:AAHjy3kFo7XgpujwF_YCkR0e86AhPJ40HG0'

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['start'])
def hello(message):
        bot.send_message(message.chat.id, 'Третья колонна следит чтобы у 8 отряда было всё плохо. Поэтому когда получилось отправить Мишу домой, мы похитили твоего напарника, если хочешь его вернуть, следуй указаниям. Приходи на точку, отвечай на вопрос мне в лс, получай кусочки ег координат. Можешь пользоваться рацией, но скорее всего тебе никто не поможет')
        bot.send_message(message.chat.id, "Первая точка - там где 24/7 играет музыка!")
        bot.register_next_step_handler(message, zero_task)

@bot.message_handler(content_types=['text'])

def zero_task(message):
    if (message.text.lower() == "галина") or (message.text.lower() == 'галя'):
        bot.send_message(message.chat.id, "1. '55.'")
        bot.send_message(441680952, "прошла первое испытание")
        bot.send_message(message.chat.id, "Вторая точка - место где мы впервые встретились!")
        bot.register_next_step_handler(message, first_task)
    else:
        bot.send_message(message.chat.id, "Нет:( ")
        bot.register_next_step_handler(message, zero_task)

def first_task(message):
    if (message.text.lower() == '21'):
        bot.send_message(message.chat.id, "2. '70'")
        bot.send_message(441680952, "прошла второе испытание")
        bot.send_message(message.chat.id, "Третья точка - обитель жрачки!")
        bot.register_next_step_handler(message, second_task)
    else:
        bot.send_message(message.chat.id, "Нет:(")
        bot.register_next_step_handler(message, first_task)

def second_task(message):
    if (message.text.lower() == 'викторович'):
        bot.send_message(message.chat.id, "3. '23'")
        bot.send_message(441680952, "прошла третье испытание")
        bot.send_message(message.chat.id, "Четвёртая точка - искраградская прорубь!")
        bot.register_next_step_handler(message, third_task)
    else:
        bot.send_message(message.chat.id, "Нет:(")
        bot.register_next_step_handler(message, second_task)

def third_task(message):
    if (message.text.lower() == '2'):
        bot.send_message(message.chat.id, "4. '23'")
        bot.send_message(441680952, "прошла четвёртое испытание")
        bot.send_message(message.chat.id, "Пятая точка - стул, на котором позавчера ночью сидел Вася, а должна была ты!")
        bot.register_next_step_handler(message, fourth_task)
    else:
        bot.send_message(message.chat.id, "Нет:(")
        bot.register_next_step_handler(message, third_task)

def fourth_task(message):
    if (message.text.lower() == '77'):
        bot.send_message(message.chat.id, "5. ' 38.'")
        bot.send_message(441680952, "прошла пятое испытание")
        bot.send_message(message.chat.id, "Шестая точка - детская комната полиции!")
        bot.register_next_step_handler(message, fifth_task)
    else:
        bot.send_message(message.chat.id, "Нет:(")
        bot.register_next_step_handler(message, fourth_task)

def fifth_task(message):
    if (message.text.lower() == '51'):
        bot.send_message(message.chat.id, "6. '10'")
        bot.send_message(441680952, "прошла шестое испытание")
        bot.send_message(message.chat.id, "Седьмая точка - свято место пусто не бывает!")
        bot.register_next_step_handler(message, sixth_task)
    else:
        bot.send_message(message.chat.id, "Нет:(")
        bot.register_next_step_handler(message, fifth_task)

def sixth_task(message):
    if (message.text.lower() == 'саша'):
        bot.send_message(message.chat.id, "7. '71'")
        bot.send_message(441680952, "прошла седьмое испытание")
        bot.send_message(message.chat.id, "Восьмая точка - Комната первой напарницы Васи!")
        bot.register_next_step_handler(message, seventh_task)
    else:
        bot.send_message(message.chat.id, "Нет:(")
        bot.register_next_step_handler(message, sixth_task)

def seventh_task(message):
    if (message.text.lower() == 'хлеб'):
        bot.send_message(message.chat.id, "8. '36'")
        bot.send_message(441680952, "прошла восьмое испытание")
        bot.send_message(message.chat.id, "Он тебя ждёт:)")
    else:
        bot.send_message(message.chat.id, "Нет:(")
        bot.register_next_step_handler(message, seventh_task)
    
    

bot.polling()
        


