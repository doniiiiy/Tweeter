import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6262014286:AAEKyy7mxDJkbslLdLiDrYP8WCwdsWUxfe8'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
# savol 1
@dp.message_handler(text="matematika")
async def echo(message: types.Message):
    await message.answer_poll(
        question="1+1",
        options=["3","1","2"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz",
    )

    await asyncio.sleep(3)

    # savol 2
    await message.answer_poll(
        question="10x10",
        options=["100","10","1"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz",
    )
    await asyncio.sleep(3)
    # savol 3
    await message.answer_poll(
        question="2x2",
        options=["5","4","3"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz",
    )


    await asyncio.sleep(3)
    # savol 3
    await message.answer_poll(
        question="Число, у которого нет собственного числа?",
        options=["1","0","10"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz",
    )


    await asyncio.sleep(3)
    # savol 3
    await message.answer_poll(
        question="Какое фактический чистый номер после 7?",
        options=["8","10","11"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz",
    )


    await asyncio.sleep(3)
    # savol 3
    await message.answer_poll(
        question="Каков фактический чистый номер после 7?",
        options=["11","12","13"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz",
    )


    await asyncio.sleep(3)
    # savol 3
    await message.answer_poll(
        question="Какое самое популярное счастливое число от 1 до 9?",
        options=["8","7","5"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz",
    )


    await asyncio.sleep(3)
    # savol 3
    await message.answer_poll(
        question="Назовите единственное четное простое число?",
        options=["2","3","1"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz",
    )


    await asyncio.sleep(3)
    # savol 3
    await message.answer_poll(
        question=" Сколько секунд в одном дне?",
        options=["86,400","86,000","55,000"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz",
    )


    await asyncio.sleep(3)
    # savol 3
    await message.answer_poll(
        question="Сколько миллиметров в одном литре?",
        options=["1500","2000","1000"],
        is_anonymous=False,
        correct_option_id=0,
        type="quiz",
    )


    await asyncio.sleep(3)
    # savol 3
    await message.answer_poll(
        question="9*N равно 108.",
        options=["N=12","N=18","N=2"],
        is_anonymous=False,
        correct_option_id=1,
        type="quiz",
    )


    await asyncio.sleep(3)
    # savol 3
    await message.answer_poll(
        question=" Какое число считается «магическим числом»?",
        options=["7","8","9"],
        is_anonymous=False,
        correct_option_id=2,
        type="quiz",
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)