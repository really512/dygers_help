from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("help"))
async def help_handler(message: Message) -> None:
    await message.answer(
        "🆘 Dygers Help\n\n"
        "/start — запустить бота\n"
        "/help — помощь\n"
        "/server — информация о сервере\n"
        "/donate — информация о донате\n"
        "/rules — правила\n"
        "/support — поддержка"
    )
