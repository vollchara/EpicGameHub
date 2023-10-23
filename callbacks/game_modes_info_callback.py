from aiogram import Router, F, types
from aiogram.exceptions import TelegramBadRequest

from keyboards.user_keyboards import user_keyboards

router = Router()

@router.callback_query(F.data.in_(["game_mode_1", "game_mode_2", "game_mode_3", "game_mode_4"]))
async def game_modes_info_callback(callback: types.CallbackQuery) -> None:
    try:
        if callback.data == "game_mode_1":
            await callback.message.edit_text("Инструкция для игрового_режима 1", reply_markup=user_keyboards.game_modes_info())
            await callback.answer()
        elif callback.data == "game_mode_2":
            await callback.message.edit_text("Инструкция для игрового_режима 2", reply_markup=user_keyboards.game_modes_info())
            await callback.answer()
        elif callback.data == "game_mode_3":
            await callback.message.edit_text("Инструкция для игрового_режима 3", reply_markup=user_keyboards.game_modes_info())
            await callback.answer()
        elif callback.data == "game_mode_4":
            await callback.message.edit_text("Инструкция для игрового_режима 4", reply_markup=user_keyboards.game_modes_info())
            await callback.answer()
    except TelegramBadRequest:
        pass