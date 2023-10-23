from typing import Any, Union

from aiogram.filters import BaseFilter
from aiogram.types import Message

from config_reader import config

class isAdmin(BaseFilter):
    def __init__(self):
        self.admin_ids = config.admin_ids.get_secret_value()
        
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in [int(id) for id in self.admin_ids.split(',')]