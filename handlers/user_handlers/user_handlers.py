import textwrap

from aiogram import Bot, Router, F, types, html
from aiogram.enums import ChatType
from aiogram.filters import Command
from aiogram.exceptions import TelegramForbiddenError

from data import database
from filters.chat_type_filter import ChatTypeFilter
from filters.is_admin_filter import isAdmin
from keyboards.user_keyboards import user_keyboards

router = Router()

@router.message(
    ChatTypeFilter(["private"]),
    Command("start")
)
async def cmd_start(message: types.Message) -> None:
    """
    This handler receives message with "/start" command.
    """
    if await database.get_user(message.from_user.id) is None:
        await database.insert_users(message.from_user.id, message.from_user.first_name)
        
        await message.answer(
            textwrap.dedent(
                f"""
                {html.bold(html.quote(await database.get_name(message.from_user.id)))}, добро пожаловать!
                {html.bold(html.quote("Epic Game Hub"))} = твоё место для развлечений и игр.
                
                Используй /help, что бы узнать о игровых режимах.
                Нажми кнопку ниже, что бы добавить бота в чат.
                """
            ), reply_markup=user_keyboards.add_bot_to_chat()
        )
    else: 
        await message.answer(
            textwrap.dedent(
                f"""
                {html.bold(html.quote(await database.get_name(message.from_user.id)))}, с возвращением!
                {html.bold(html.quote("Epic Game Hub"))} = твоё место для развлечений и игр.
                
                Используй /help, что бы узнать о игровых режимах.
                Нажми кнопку ниже, что бы добавить бота в чат.
                """
            ), reply_markup=user_keyboards.add_bot_to_chat()
        )


@router.message(Command("help"))
async def cmd_help(message: types.Message, bot: Bot) -> None:
    if message.chat.type == ChatType.PRIVATE:
        await message.answer(
            textwrap.dedent(
                f"""
                Справка {html.bold(html.quote("Epic Game Hub"))}!
                
                {html.bold(html.quote("Epic Game Hub"))} - многофункциональный чат-бот, предназначенный для организации различных игровых режимов.
                Используй кнопки, что бы ознакомиться с правилами и механиками каждой из доступных игр.
                """
            ), reply_markup=user_keyboards.game_modes_info()
        )
    else:
        try:
            await bot.send_message(
                message.from_user.id,
                textwrap.dedent(
                    f"""
                    Справка {html.bold(html.quote("Epic Game Hub"))}!
                    
                    {html.bold(html.quote("Epic Game Hub"))} - многофункциональный чат-бот, предназначенный для организации различных игровых режимов.
                    Используй кнопки, что бы ознакомиться с правилами и механиками каждой из доступных игр.
                    """
                ), reply_markup=user_keyboards.game_modes_info()
            )
        except TelegramForbiddenError:
            await message.reply(
                textwrap.dedent(
                    f"""
                    {html.bold(html.quote(await database.get_name(message.from_user.id)))}, я не могу писать тебе личные сообщения.
                    Напиши мне команду /start и повтори попытку. 
                    """
                )
            )

