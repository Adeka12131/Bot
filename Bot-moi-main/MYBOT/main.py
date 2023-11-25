from config import *
from aiogram import types, Bot, Dispatcher, executor
from aiogram.types import InputFile

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    await bot.send_message(chat_id=OWNER_ID,text='Здравствуйте что если вы хотите начать с вопросов о нашей компании то вам стоит нажать /start')

main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
b_quest3 = types.KeyboardButton('Кто вы такие?')
b_quest4 = types.KeyboardButton('Как с вами связаться?')
main_keyboard.row(b_quest3).add(b_quest4)

question1_kb = types.InlineKeyboardMarkup()
question1 = types.InlineKeyboardButton(text="О нас 🧑🏻‍💻",callback_data="Занимаемся чем то")
question2 = types.InlineKeyboardButton(text="Чем мы занимаемся❔",callback_data="Что мы делаем")
question4 = types.InlineKeyboardButton(text="Наши особенности✨",callback_data="почему именно мы")
question1_kb.add(question1).add(question2).add(question4)

question3_kb = types.InlineKeyboardMarkup()
question3 = types.InlineKeyboardButton(' По Whatsapp',url = 'https://web.whatsapp.com/:')
question5 = types.InlineKeyboardButton(' По Telegram',url = 'https://web.telegram.org/')
question6 = types.InlineKeyboardButton(' По Instagram',url = 'https://www.instagram.com/:')
question3_kb.add(question3).add(question5).add(question6)

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    photo_path = (r"C:\Users\User\OneDrive\Рабочий стол\кот\Кот.jpg.jpg")
    await message.answer('Здравствуйте! Я бот команды WorkBench. Чем могу помочь сегодня?', reply_markup=main_keyboard)
    await bot.send_photo(message.chat.id, InputFile(photo_path))


@dp.callback_query_handler(lambda callback_query: True)
async def handle_callback_query(callback_query: types.CallbackQuery):
    if callback_query.data == "Занимаемся чем то":
        await bot.send_message(callback_query.from_user.id, '''Мы - одно из самых быстрорастущих агенств🌐
Занимаемся созданием веб-интерфейсов, мобильных приложений, телеграмм-ботов. 
Также у нас происходит оплачиваемая стажировка(т.е. обучение) с будущей возможностью присоединиться к нам в команду! ⚡''')
    elif callback_query.data == "Что мы делаем":
        await bot.send_message(callback_query.from_user.id, '''Мы разрабатываем сайты и мобильные приложения, пишем телеграмм боты,а также создаем UI/UX дизайн👩🏻‍🎨
Также мы принимаем стажеров на обучение. Изучение языков html5, css3, java script, node js, REACT и python.📚''')
    elif callback_query.data == "почему именно мы":
        await bot.send_message(callback_query.from_user.id,
'''Наш главный плюс - это бесплатное предоставление логотипа компании при любом заказе🤘
В своих задачах,мы используем креативный и индивидуальный подход, тщательно проанализируя продукт и конкурентов.😎 
У нас есть несколько этапов разработки. Прежде чем пустить продукт на рынок,мы качественно тестируем его. Также у нас очень короткие сроки выполнения, низкие цены и отличное качество💰☺️
        ''')

@dp.message_handler()
async def main_message(message: types.Message):
    if message.text == 'Кто вы такие?':
        await message.answer('Выберите интересующий вас вопрос:', reply_markup=question1_kb)
    elif message.text == 'Как с вами связаться?':
        await message.answer('По ватсапп',reply_markup=question3_kb)

        
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    