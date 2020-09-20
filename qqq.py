import telebot
from time import sleep

bot = telebot.TeleBot('1269869434:AAEkbfZo237E-grvjRKKSd_GEu1d_hbSAlU')

io = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
io.row('🔑 Вход')

uuu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
uuu.row('💰 Кошелек', '💳 Магазин')
uuu.row('💵 Обналичивание', '💰 Чекер баланса')
uuu.row('💸 Чекер на валидность', '📃 Помощь')

xui = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
xui.row('✋🏻 Ручное обналичивание', '⚙️ Автоматическое обналичивание')
xui.row('⬅️ Назад')

sus = telebot.types.InlineKeyboardMarkup()
pisk = telebot.types.InlineKeyboardButton(text='💸 Купить', callback_data='buy')
sus.add(pisk)

inline = telebot.types.InlineKeyboardMarkup()
lol = telebot.types.InlineKeyboardButton(text='💰Пополнить', callback_data='plus')
kek = telebot.types.InlineKeyboardButton(text='💸 Вывести', callback_data='minus')
inline.add(lol, kek)

lalka = telebot.types.InlineKeyboardMarkup()
mda = telebot.types.InlineKeyboardButton(text='🔎 Проверить платеж', callback_data='check')
lalka.add(mda)

anime = telebot.types.InlineKeyboardMarkup()
rai = telebot.types.InlineKeyboardButton(text='💳 VISA (Баланс от 10000)', callback_data='tenk')
rau = telebot.types.InlineKeyboardButton(text='💳 MASTERCARD (Баланс от 5000)', callback_data='fivek')
rak = telebot.types.InlineKeyboardButton(text='💳 МИР (Баланс от 3000)', callback_data='trik')
ral = telebot.types.InlineKeyboardButton(text='💳 РАНДОМ (Баланс от 1 до 100000)', callback_data='stok')
rao = telebot.types.InlineKeyboardButton(text='🍔 СХЕМА ВБИВА ЕДЫ', callback_data='eda')
anime.add(rai)
anime.add(rau)
anime.add(rak)
anime.add(ral)
anime.add(rao)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Авторизуйтесь чтобы вы могли работать с ботом', reply_markup=io)
    
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == '🔑 Вход':   
        bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=uuu)    
    if message.text == '💰 Кошелек': 
        bot.send_message(message.chat.id, 'Ваш баланс: 0 BTC', reply_markup=inline)
    if message.text == '💳 Магазин':
        bot.send_message(message.chat.id, '🎫 В магазине предоставлены валидные карты с балансами\nВозврат средств/замена товара в случае невалида', reply_markup=anime)
    if message.text == '💵 Обналичивание':
        bot.send_message(message.chat.id, '<b>⚡️ В данном разделе вы можете обналичить карты в двух режимах:</b>\n\n1)Ручной режим - обнал осуществляется вручную нашей командой\n2)Автоматический - обнал происходит через наши приватные сервисы', parse_mode='html', reply_markup=xui)    
    if message.text == '💰 Чекер баланса':
        bot.send_message(message.chat.id, 'Введите данные карты в формате:\nXXXXXXXXXXXXXXXX | XX/XX | XXX\nСтрого учитывайте разделитель "|"\nТак же можно загрузить базу карт в аналогичном формате в каждой строчке')
    if message.text == '💸 Чекер на валидность':
        bot.send_message(message.chat.id, '⚡️ Соединяемся с банком')
        sleep(4)
        bot.send_message(message.chat.id, '✳️ Принимаем ответ')
        sleep(2)
        bot.send_message(message.chat.id, '✅ Ответ получен')
        sleep(3)
        bot.send_message(message.chat.id, 'Результат теста: ❌ Неверный ввод данных')
    if message.text == '📃 Помощь':    
        bot.send_message(message.chat.id, 'В нашем боте вы сможете проверить баланс, проверить валидность и обналичить карты в биткоин. Выберите нужное действие и следуйте инструкции. На данный момент идет разработка возможности обналичивать не только карты РФ.\n\nРазработчик бота @badboyee')
    if message.text == '✋🏻 Ручное обналичивание':
        bot.send_message(message.chat.id, 'Введите сумму:')
    if message.text == '⚙️ Автоматическое обналичивание': 
        bot.send_message(message.chat.id, 'Введите сумму:')
    if message.text == '⬅️ Назад':
        bot.send_message(message.chat.id, '✅ Вы успешно вернулись в главное меню', reply_markup=uuu)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
        if call.data == 'plus':
            bot.send_message(call.message.chat.id, '<b>🆙 Пополнение баланса\n\n🔅 Номер: +799999999999\n🔅 Сумма  от 1 до 15000 рублей\n🔅 Комментарий к платежу:</b> 457202\n\n♻️ После перевода нажмите кнопку проверить', parse_mode='html', reply_markup=lalka)        
        if call.data == 'minus':
            bot.send_message(call.message.chat.id, '<b>⚠️ Минимальная сумма вывода: 750 рублей</b>', parse_mode='html')
        if call.data == 'check':
            bot.send_message(call.message.chat.id, '<b>Подождите...</b>', parse_mode='html')   
            sleep(5)
            bot.send_message(call.message.chat.id, '<b>⚠️ Платеж не найден</b>', parse_mode='html')   
        if call.data == 'buy':
            bot.send_message(call.message.chat.id, '<b>⚠️ Недостаточно средств, пополните кошелек</b>', parse_mode='html')
        if call.data == 'tenk':
            bot.send_message(call.message.chat.id, '<b>💳 VISA</b>\n\n<b>💵 Баланс:</b> от 10000 РУБ.\n<b>💸 Цена:</b> 2000 РУБ.\n\nДля оплаты нажмите кнопку "Купить"', parse_mode='html', reply_markup=sus)
        if call.data == 'fivek':
            bot.send_message(call.message.chat.id, '<b>💳 MASTERCARD</b>\n\n<b>💵 Баланс:</b> от 5000 РУБ.\n<b>💸 Цена:</b> 1000 РУБ.\n\nДля оплаты нажмите кнопку "Купить"', parse_mode='html', reply_markup=sus)
        if call.data == 'trik':
            bot.send_message(call.message.chat.id, '<b>💳 МИР</b>\n\n<b>💵 Баланс:</b> от 3000 РУБ.\n<b>💸 Цена:</b> 500 РУБ.\n\nДля оплаты нажмите кнопку "Купить"', parse_mode='html', reply_markup=sus)
        if call.data == 'stok':
            bot.send_message(call.message.chat.id, '<b>💳 РАНДОМ</b>\n\n<b>💵 Баланс:</b> от 1 РУБ до 100000 РУБ.\n<b>💸 Цена:</b> 50 РУБ.\n\nДля оплаты нажмите кнопку "Купить"', parse_mode='html', reply_markup=sus)
        if call.data == 'eda':
            bot.send_message(call.message.chat.id, '<b>🍔 СХЕМА ПО ВБИВУ ЕДЫ</b>\n\nЗаказ еды из Delivery от 3000 РУБ. (Мануал + полная поддержка)\n<b>💸 Цена:</b> 2000Р.\n\nДля оплаты нажмите кнопку "Купить"', parse_mode='html', reply_markup=sus)       
    
bot.polling(none_stop=True)