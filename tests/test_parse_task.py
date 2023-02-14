import os

from src import parse

task = '#задача  \n' \
       'Написать бота  \n' \
       'Гудков  \n' \
       'Ханов  ,     Макурин  \n' \
       'до 12:30 01.03.22   \n' \
       '  сделайте     пожалуйста бота \n' \
       'очень сука блин нужно '

t = parse.message(task)
print(t)
