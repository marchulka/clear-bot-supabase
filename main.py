from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import openai
import os

from config.settings import TELEGRAM_TOKEN, OPENAI_API_KEY

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)
openai.api_key = OPENAI_API_KEY

SYSTEM_PROMPT = "Ты — вежливый и внимательный AI-ассистент. Отвечай кратко, по делу, избегай догадок."

@dp.message_handler()
async def handle_message(message: Message):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message.text}
        ]
    )
    reply = response.choices[0].message["content"]
    await message.reply(reply)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)