import telebot

Task =''
photo_url='https://sun9-24.userapi.com/impg/VZSnyLc8cFTCGIhTqeTaodOeL4SGXVYai6tbgA/RxGVPePeOl0.jpg?size=1200x1600&quality=95&sign=27c1e143842792fa7ab81876d246871c&type=album'
API_KEY = '6566238196:AAFBYeK73uker_7HkFNGwzNM_2HM1YIkvIk'

bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['start'])
def hello(message):
        bot.send_message(message.chat.id, 'Да, это высокотехнологичная штуковина для тебя, милая! Ты уже почти-почти взрослая (но для меня всегда останешься малышкой:)). Столько всего было в твоей жизни. Давай посмотрим, всё ли ты помнишь?)')
        bot.send_message(message.chat.id, "Тебе будут задаваться вопросы, за правильный ответ на которые, ты будешь получать буковки. Надеюсь ты догадаешься, что с ними делать. Вопросы будут приходить тебе каждые 10 минут начиная с 22:59. У тебя есть телефон, пользуйся всеми его возможностями, ответы у тебя есть на все вопросы, просто надо знать, где искать! Ну или звони в тех.поддержку за подсказками: +79197299166")
        bot.send_message(message.chat.id, "Начнём с детства. Помнишь этот сладкий вкус белой густой субстанции, которую можно было есть ложками из банки и совсем не запивать чаем. Вопрос: В какую сторону смотрел носик чайника?")
        bot.register_next_step_handler(message, zero_task)

@bot.message_handler(content_types=[' text'])

def zero_task(message):
    if (message.text.lower() == "направо") or (message.text.lower() == 'вправо') or (message.text.lower() == 'право'):
        bot.send_message(message.chat.id, "L")
        bot.send_message(441680952, "прошла первое испытание")
        bot.send_message(message.chat.id, "У тебя столько замечательных родственников... А всё ли ты знаешь о них? После первого свидания ты застала меня врасплох, задав один вопрос. Моя очередь:) Вопрос: Какого цвета балкон у Татьяны Федоровны. (варианты: белый, серый, черный, коричневый, синий, зеленый, бордовый, красный, оранжевый, фиолетовый, жёлтый, голубой, рыжий, салатовый, цвет морской волны, цвет морской волны в геленджике, бирюзовый, берёзовый, пастельный, нюдовый, нюдсовы и т.д.)")
        bot.register_next_step_handler(message, first_task)
    else:
        bot.send_message(message.chat.id, "Нет:( ")
        bot.register_next_step_handler(message, zero_task)

def first_task(message):
    if (message.text.lower() == 'серый'):
        bot.send_message(message.chat.id, "e")
        bot.send_message(441680952, "прошла второе испытание")
        bot.send_message(message.chat.id, "А это птица-(???????), на которой летишь в место, где свежий воздух и у печки спится. в том месте не можешь угомониться, идти на речку, кушать смородину и веселиться в дом который построила Ока луговая. Ну?")
        bot.register_next_step_handler(message, second_task)
    else:
        bot.send_message(message.chat.id, "Нет:(")
        bot.register_next_step_handler(message, first_task)

def second_task(message):
    if (message.text.lower() == 'кукушка'):
        bot.send_message(message.chat.id, "t")
        bot.send_message(441680952, "прошла третье испытание")
        bot.send_message(message.chat.id, "По-тихоньку ты начала взрослеть и путешествовать. Однажды мы с тобой отправились в путешествие вместе. Какой бы ты взрослой не была, я всё равно чувствовал, чувствую и буду чувствовать за тебя ответственность. Вопрос: На месте с каким номером ты ехала?")
        bot.register_next_step_handler(message, third_task)
    else:
        bot.send_message(message.chat.id, "Нет:(")
        bot.register_next_step_handler(message, second_task)

def third_task(message):
    if (message.text.lower() == '23' or message.text.lower() == '023'):
        bot.send_message(message.chat.id, "s")
        bot.send_message(441680952, "прошла четвёртое испытание")
        bot.send_message(message.chat.id, "А там дальше пошли и шуры и муры, короче - любовь! Свиданки, киношки. Сколько раз мы там были - одному папе известно. Вопрос: оригинальное название фильма 'Руслан и мустафинцы'(да, мы его смотрели в одном из наших с тобой любимых кинотеатров)")
        bot.register_next_step_handler(message, fourth_task)
    else:
        bot.send_message(message.chat.id, "Нет:(")
        bot.register_next_step_handler(message, third_task)

def fourth_task(message):
    if (message.text.lower() == 'артур и минипуты'):
        bot.send_message(message.chat.id, "a")
        bot.send_message(441680952, "прошла пятое испытание")
        bot.send_message(message.chat.id, "Ну и как я мог не затронуть девочку нашу, бусинку, малышку, кошечку и т.д. Чмокни её за меня. Вопрос: Какая была подпись у этой фотографии?")
        bot.send_photo(message.chat.id, photo=photo_url)
        bot.register_next_step_handler(message, fifth_task)
    else:
        bot.send_message(message.chat.id, "Нет:(")
        bot.register_next_step_handler(message, fourth_task)

def fifth_task(message):
    if (message.text.lower() == 'стелла делает апап'):
        bot.send_message(message.chat.id, "l")
        bot.send_message(441680952, "прошла шестое испытание")
        bot.send_message(message.chat.id, "Умничка! А теперь думай, что с этим делать. Пока-пока:)")
    else:
        bot.send_message(message.chat.id, "Нет:(")
        bot.register_next_step_handler(message, seventh_task)
        

bot.polling()
        


