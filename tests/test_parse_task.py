import os

from src.parsing.parse import parse_message

task = '#задача  \n' \
       'Написать бота  \n' \
       'Гудков  \n' \
       'Ханов  ,     Макурин  \n' \
       'до 01.03  \n' \
       '  сделайте     пожалуйста бота  '

os.chdir('..')
t = parse_message(task)
print(t)
