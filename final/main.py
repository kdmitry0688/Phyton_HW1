from bs4 import BeautifulSoup
import requests
import telebot
from telebot import types
token = '5975972785:AAHX9Yr9amgpCq_3kKUaKUTFQU4k08rneYk'
appid = 'bda0f28015d9c9ff32237df0cd9e4dd3'


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Погода")
    item2 = types.KeyboardButton("Гороскоп")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Привет ✌️, выберите что вам надо',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
		menu1 = types.InlineKeyboardMarkup(row_width = 2)
		item1 = types.InlineKeyboardButton(text='Караганда', callback_data='krg')
		item2 = types.InlineKeyboardButton(text='Алма-Ата', callback_data='alm')
		menu1.add(item1, item2)

		menu2 = types.InlineKeyboardMarkup(row_width = 2)
		item1 = types.InlineKeyboardButton(text='Овен', callback_data='oven')
		item2 = types.InlineKeyboardButton(text='Телец', callback_data='telec')
		item3 = types.InlineKeyboardButton(text='Близнецы', callback_data='bliznec')
		item4 = types.InlineKeyboardButton(text='Рак', callback_data='rak')
		item5 = types.InlineKeyboardButton(text='Лев', callback_data='lev')
		item6 = types.InlineKeyboardButton(text='Дева', callback_data='deva')
		item7 = types.InlineKeyboardButton(text='Весы', callback_data='vesi')
		item8 = types.InlineKeyboardButton(text='Скорпион', callback_data='scorp')
		item9 = types.InlineKeyboardButton(text='Стрелец', callback_data='strelec')
		item10 = types.InlineKeyboardButton(text='Козерог', callback_data='kozerog')
		item11 = types.InlineKeyboardButton(text='Водолей', callback_data='vodolei')
		item12 = types.InlineKeyboardButton(text='Рыбы', callback_data='riba')
		menu2.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)



		if message.text == "Погода":
			bot.send_message(message.chat.id, text = "Выберите город", reply_markup = menu1)
		if message.text == "Гороскоп":
			bot.send_message(message.chat.id, text = "Выберите знак зодиака", reply_markup = menu2)



@bot.callback_query_handler(func=lambda call: True)
def step2(call):
	if call.data == 'krg':
		bot.send_message(call.message.chat.id, 'Сейчас выведу погоду в Караганде')
		ow = request_current_weather(609655)
		bot.send_message(call.message.chat.id, f'{ow[0].capitalize()}\nТекущая температура: {ow[1]} °C\nВидимость: {ow[2]} м\nСкорость ветра: {ow[3]} м/с')
	elif call.data == 'alm':
		bot.send_message(call.message.chat.id, 'Сейчас выведу погоду в Алма-Ате')
		ow = request_current_weather(1526384)
		bot.send_message(call.message.chat.id, f'{ow[0].capitalize()}\nТекущая температура: {ow[1]} °C\nВидимость: {ow[2]} м\nСкорость ветра: {ow[3]} м/с')
	elif call.data == 'oven':
		bot.send_message(call.message.chat.id, 'Овен, гороскоп на сегодня')
		ow = connect_parser('aries')
		bot.send_message(call.message.chat.id, f'{ow}')
	elif call.data == 'telec':
		bot.send_message(call.message.chat.id, 'Телец, гороскоп на сегодня')
		ow = connect_parser('taurus')
		bot.send_message(call.message.chat.id, f'{ow}')
	elif call.data == 'bliznec':
		bot.send_message(call.message.chat.id, 'Близнец, гороскоп на сегодня')
		ow = connect_parser('gemini')
		bot.send_message(call.message.chat.id, f'{ow}')
	elif call.data == 'rak':
		bot.send_message(call.message.chat.id, 'Рак, гороскоп на сегодня')
		ow = connect_parser('cancer')
		bot.send_message(call.message.chat.id, f'{ow}')
	elif call.data == 'lev':
		bot.send_message(call.message.chat.id, 'Лев, гороскоп на сегодня')
		ow = connect_parser('leo')
		bot.send_message(call.message.chat.id, f'{ow}')
	elif call.data == 'deva':
		bot.send_message(call.message.chat.id, 'Дева, гороскоп на сегодня')
		ow = connect_parser('virgo')
		bot.send_message(call.message.chat.id, f'{ow}')
	elif call.data == 'vesi':
		bot.send_message(call.message.chat.id, 'Весы, гороскоп на сегодня')
		ow = connect_parser('libra')
		bot.send_message(call.message.chat.id, f'{ow}')
	elif call.data == 'scorp':
		bot.send_message(call.message.chat.id, 'Скорпион, гороскоп на сегодня')
		ow = connect_parser('scorpio')
		bot.send_message(call.message.chat.id, f'{ow}')
	elif call.data == 'strelec':
		bot.send_message(call.message.chat.id, 'Стрелец, гороскоп на сегодня')
		ow = connect_parser('sagittarius')
		bot.send_message(call.message.chat.id, f'{ow}')
	elif call.data == 'kozerog':
		bot.send_message(call.message.chat.id, 'Козерог, гороскоп на сегодня')
		ow = connect_parser('capricorn')
		bot.send_message(call.message.chat.id, f'{ow}')
	elif call.data == 'vodolei':
		bot.send_message(call.message.chat.id, 'Водолей, гороскоп на сегодня')
		ow = connect_parser('aquarius')
		bot.send_message(call.message.chat.id, f'{ow}')
	elif call.data == 'riba':
		bot.send_message(call.message.chat.id, 'Рыбы, гороскоп на сегодня')
		ow = connect_parser('pisces')
		bot.send_message(call.message.chat.id, f'{ow}')


def request_current_weather(city_id):
	res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
	data = res.json()
	conditions = data['weather'][0]['description']
	temp = data['main']['temp']
	visibility = data['visibility']
	wind = data['wind']['speed']
	return conditions, temp, visibility, wind


def connect_parser(zodiac_sign):
	url = f'https://horo.mail.ru/prediction/{zodiac_sign}/today/'
	response = requests.get(url)
	bs = BeautifulSoup(response.text, 'lxml')
	
	temp = bs.find('div', class_='article__item article__item_alignment_left article__item_html').text
	return temp






bot.infinity_polling()
