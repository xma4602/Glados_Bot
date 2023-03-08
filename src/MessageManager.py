from src.bot.Notice import Notice
from datetime import datetime

from src.bot import vk_bot


def send(notice: Notice):
    vk_bot.send(notice.message_everyone())


def plan(notice: list):
    pass
