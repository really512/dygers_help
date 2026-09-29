from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(
        "👋 Привет! Я Dygers Help — бот помощи Dygers.\n\n"
        "Используй /help, чтобы посмотреть доступные команды."
    )
