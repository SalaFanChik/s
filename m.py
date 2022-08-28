import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import random 

API_TOKEN = '5730098464:AAEOudiLDXx_62WZ4EsDmUQjV1Lk0N4GnxM'

# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

inline_btn_1 = InlineKeyboardButton('Получить комплимент!', callback_data='button1')
inline_btn_2 = InlineKeyboardButton('Получить фото', callback_data='button2')
inline_btn_3 = InlineKeyboardButton('Написать любимому(мна жерге озимди мактап макатап жазып кою керек ед)', url="https://wa.me/+77714567822")
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
inline_kb1.row(inline_btn_2)
inline_kb1.add(inline_btn_3)

inline_btn_4 = InlineKeyboardButton('На главную', callback_data='button4')
inline_kb2 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_4)

inline_kb3 = InlineKeyboardMarkup().add(inline_btn_2, inline_btn_4)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    if message.from_user.id == 1366082751 or 1639491822:
        await message.answer("Добро пожаловать в Наш Мир, Моя Королева!\nЭтот был создан от чистого сердца! знаю и так часто говорю ласковые слова и как сильно люблю тебя, но если тебе не достаточное, можешь писать мне а не боту! \n\n\n С любовью твой Алихан❤️❤️", reply_markup=inline_kb1)

@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_callback_button2(callback_query: types.CallbackQuery):
    choice = random.choice(['AgACAgIAAxkBAAMFYvu9v8k-pveYfZwHoaxHGqUNHNAAAg_CMRul3-FK5UHQy_wLRqUBAAMCAANzAAMpBA', 'AgACAgIAAxkBAAMGYvu9_UAoXCGWO5kvIZJUqhD0Q70AAhDCMRul3-FKzrfgkFIkmrABAAMCAANzAAMpBA', 'AgACAgIAAxkBAAMHYvu-AoYXeMyyKGrgk4KNuZ4w1MEAAhLCMRul3-FK4AmIyXJnWbwBAAMCAANzAAMpBA', 'AgACAgIAAxkBAAMIYvu-BjEMEcWwr6eg84nTEJ3gdjMAAhPCMRul3-FKDzWlPJq7_3UBAAMCAANzAAMpBA', 'AgACAgIAAxkBAAMJYvu_R-i_7EbjDNYUDXj4CYiLNw4AAp-_MRsd7eBLI3JSRw-oegwBAAMCAANzAAMpBA', 'AgACAgIAAxkBAAMKYvvBQ7hrph14riWi6xhrptPdA4IAAru-MRsgTLFLDR5hViRJkY4BAAMCAANzAAMpBA', 'AgACAgIAAxkBAAMOYvvBmv_5Qy2D1rOUvSZ7Z9bFDvQAAn_CMRuYDOFLOMidaWAZSdcBAAMCAANzAAMpBA', 'AgACAgIAAxkBAAMPYvvCJvQWDEpJejB-_GiCr9g9zfQAAoHCMRuYDOFLJ05Pf1QAAZ8kAQADAgADcwADKQQ', 'AgACAgIAAxkBAAMQYvvCJhHg0siQcsgYz4Lzc3GCQ4EAAoLCMRuYDOFLHGk9SC9XIrwBAAMCAANzAAMpBA', 'AgACAgIAAxkBAAMRYvvCJofHsdo3wFTmc6XQXxDD3q0AAoPCMRuYDOFLifjexg0IYo4BAAMCAANzAAMpBA', 'AgACAgIAAxkBAAMSYvvCJhIzJNE3Gk5kGl1_mlEalUoAAoTCMRuYDOFLuqYoD2mqfNkBAAMCAANzAAMpBA',])
    await bot.send_photo(callback_query.from_user.id, choice, reply_markup=inline_kb3)

@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button3(callback_query: types.CallbackQuery):
    spisok = ['Твоя улыбка восхитительна', 'Ты внутри еще красивее чем снаружи', 'У тебя отличное чувство юмора', 'Тебе ну нужен макияж для красоты скорее макияжу нужна ты', 'От твоих глаз захватывает дух', 'Ты выглядишь очень женственно и привлекательно', 'Если красота считалась преступлением то ты была бы в розыске', 'Ты вкусно и невероятно пахнешь', 'Ты настоящий подарок этому миру', 'От тебя сложно оторвать взгляд', 'Ты настоящая умница', 'Ты самая лучшая', 'Ты смеешься очень заразительно', 'У тебя безукоризненные манеры', 'Ты идеальная и сногсшибательная', 'В твоих глазах можно утонуть', 'Даже в спортивной одежде ты восхитительна', 'Мне нравится твой стиль', 'У тебя потрясающая прическа', 'По шкале от  до  ты', 'Ты выглядишь очень аппетитно', 'Ты как солнце в дождливый день', 'Ты заслуживаешь объятия прямо сейчас', 'Внимательно ходи по улицам чтобы не наступить пораженных твоей красотой мужчин', 'Ты отличный пример для подражания', 'Я никогда не встречал такую восхитительную и замечательную девушку', 'Ты очень нежная и заботливая', 'У тебя потрясающая фигура', 'В твоей прекрасной груди бьется жаркое сердце', 'Ты невероятна когда не боишься быть собой', 'Мир кажется лучше когда ты рядом', 'Ты очень мудрая', 'Ты смелая и отважная', 'Ты лучше чем сказочная принцесса', 'Ты должна гордиться собой', 'У тебя чувственные губы', 'Что делает такой ангел на земле', 'Твои ножки просто космос', 'Тебя наверняка любят маленькие детишки и даже животные', 'Ты замечательная и непостижимая девушка', 'Кто тебя воспитал Они заслуживают золотую медаль', 'Твое имя подходит тебе', 'Ты красивее чем можешь представить', 'Ты хороший собеседник', 'Твоя действия говорят больше чем слова', 'Ты вдохновляешь меня', 'Я многому научился у тебя', 'Ничего в себе не меняй', 'Ты великолепна', 'Твоя попа как крепкий орешек', 'Ты выглядишь как модель перед фотосессией', 'Твой голос очень мелодичный и волнующий', 'Ты очень естественная и настоящая', 'У тебя толковая голова на прелестных плечиках', 'Когда ты краснеешь то становишься милой', 'Ты всегда будешь поводом моей улыбки', 'Этот цвет тебе идеально подходит', 'Ты очень скромная хорошая и порядочная', 'Меня поражает твоя открытость и искренность', 'Не знал что принцессы бывают не только в сказках', 'Ты очень добрая и чуткая', 'Ты действительно особенная и неповторимая', 'Ты лучше чем мороженное с пирожным', 'Ты умна и рассудительна несмотря на юный возраст', 'Твой голос как музыка', 'Ты произведения искусства', 'Ты шоколадная сладкая конфетка', 'А где твой нимб ангелочек', 'Ты необъяснимая загадка', 'Ты обаятельная очаровательная и привлекательная', 'Ты одновременно хрупкая и сильная', 'Ты доставляешь больше удовольствие чем лопать пленку с пупырышками', 'Ты очень темпераментная и горячая', 'У тебя очень гармоничный образ', 'Ты очень заводная веселая и позитивная', 'Если бы ты жила на Кавказе тебя бы уже украли давнымдавно', 'Мир был бы прекрасен если бы таких как ты было больше', 'Я полностью обезоружен твоим остроумием', 'Ты похожа на недоступную жемчужину на дне океана', 'Я влюблен в твои глаза', 'Твоя внешность очень обольстительная', 'Ты как глоток свежего воздуха']
    await bot.send_message(callback_query.from_user.id, random.choice(spisok), reply_markup=inline_kb2)

@dp.callback_query_handler(lambda c: c.data == 'button4')
async def process_callback_button4(callback_query: types.CallbackQuery):
        await callback_query.message.answer("Добро пожаловать в Наш Мир, Моя Королева!\nЭтот был создан от чистого сердца! знаю и так часто говорю ласковые слова и как сильно люблю тебя, но если тебе не достаточное, можешь писать мне а не боту! \n\n\n С любовью твой Алихан❤️❤️", reply_markup=inline_kb1)




@dp.message_handler(content_types=['photo'])
async def send_welcome(message: types.Message):
    print(message.photo[0].file_id)
  

@dp.message_handler()
async def send_welcome(message: types.Message):
    print(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)  