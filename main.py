from vk import VK
from telegram_bot import Telegram
from parser_bot import ParserAniDubLife, ParserAnimedubRu
import asyncio


vkObj = VK('6cb02efc792b6ab73f5128fc0a2ff825456cae8daa81fc22e9b747381d41b6287e0877529ba6106ce76e8', '199231862')
telegramObj = Telegram()
parserObj_AnimedubRu = ParserAnimedubRu()
parserObj_AnimedubLife = ParserAnimedubLife()


while True:
    data_user = vkObj.wait_message()
    print(data_user)
    count = parserObj.search_on_site(data_user['text'])
    print(count)
    if count:
        info = parserObj.information_of_anime()
        #vkObj.send_message(count)
        vkObj.send_message(info)
    else:
        vkObj.send_message('dada')


if __name__ == '__main__':
    pass