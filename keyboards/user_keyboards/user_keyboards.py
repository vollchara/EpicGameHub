from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def add_bot_to_chat() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text="Добавить | Epic Game Hub | в чат",
            url="https://telegram.me/vo11chara_telegram_bot?startgroup=new"
        )
    )
    
    return builder.as_markup()

def game_modes_info() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(
            text="Игра 1",
            callback_data="game_mode_1"
        ),
        InlineKeyboardButton(
            text="Игра 2",
            callback_data="game_mode_2"
        ),
        InlineKeyboardButton(
            text="Игра 3",
            callback_data="game_mode_3"
        ),
        InlineKeyboardButton(
            text="Игра 4",
            callback_data="game_mode_4"
        )
    )
    
    builder.adjust(2)
    return builder.as_markup()