from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import openai
from config.settings import TELEGRAM_TOKEN, OPENAI_API_KEY
from logger import log_attempt

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)
openai.api_key = OPENAI_API_KEY

SYSTEM_PROMPT = "Ты — вежливый и внимательный AI-ассистент. Отвечай кратко, по делу, избегай догадок."

@dp.message_handler()
async def handle_message(message: Message):
    user_id = str(message.from_user.id)
    bot_id = (await bot.get_me()).id
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message.text}
            ]
        )
        reply = response.choices[0].message["content"]
        await message.reply(reply)

        log_attempt(
            user_id=user_id,
            bot_id=str(bot_id),
            user_input=message.text
        )
    except Exception as e:
        log_attempt(
            user_id=user_id,
            bot_id=str(bot_id),
            user_input=message.text,
            error_code="GPT_ERROR",
            error_message=str(e)
        )
        await message.reply("Произошла ошибка при обращении к ИИ.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
