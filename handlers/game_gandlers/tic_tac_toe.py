import textwrap

from aiogram import Router, F, types, html
from aiogram.enums import ChatType
from aiogram.filters import Command

from data import database
from filters.chat_type_filter import ChatTypeFilter

router = Router()

@router.message(
    ChatTypeFilter(["group", "supergroup"]),
    Command("playxando")
)
async def cmd_playxando(message: types.Message) -> None:
    if await database.get_user(message.from_user.id) is None:
        await database.insert_users(message.from_user.id, message.from_user.first_name)
        
    if (await database.get_game_activity(message.from_user.id)):
        print("Твоя игровая активность True")
        await message.reply(
            textwrap.dedent(
                f"""
                {html.bold(html.quote(await database.get_name(message.from_user.id)))}, ты не можешь играть две игры одновременно.
                Закончи начатую ранее игру и повтори попытку.
                """
            )
        )
        return
    
    if message.reply_to_message:
        if message.reply_to_message.from_user.id == message.from_user.id:
            await message.reply(
                textwrap.dedent(
                    f"""
                    {html.bold(html.quote(await database.get_name(message.from_user.id)))}, ты не можешь играть сам с собой.
                    Отправь команду /playxando в ответ на сообщение того человека, с кем хочешь сыграть.
                    """
                )
            )
        elif message.reply_to_message.from_user.is_bot:
            await message.reply(
                textwrap.dedent(
                    f"""
                    {html.bold(html.quote(await database.get_name(message.from_user.id)))}, ты не можешь играть с ботом.
                    Отправь команду /playxando в ответ на сообщение того человека, с кем хочешь сыграть.
                    """
                )
            )
        else:
            if await database.get_user(message.reply_to_message.from_user.id) is None:
                await database.insert_users(message.reply_to_message.from_user.id, message.reply_to_message.from_user.first_name)
                
            if not (await database.get_game_activity(message.reply_to_message.from_user.id)):
                print("все проверки пройдены, можете играть")
            else:
                await message.reply(
                    textwrap.dedent(
                        f"""
                        {html.bold(html.quote(await database.get_name(message.from_user.id)))}, игрок которому ты бросил вызов, уже находится в игре. 
                        Дождись пока он закончит свою игру и повтори попытку снова.
                        """
                    )
                )
    else:
        await message.reply(
            textwrap.dedent(
                f"""
                {html.bold(html.quote(await database.get_name(message.from_user.id)))}, {html.link(html.quote("чтобы бросить вызов"), link="https://t.me/vo11chara_telegram_bot")} отправь команду /plaxando в ответ на сообщение того человека, с кем хочешь сыграть.
                """
            )
        )