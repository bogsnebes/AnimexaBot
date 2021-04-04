from vk import VK
from telegram_bot import Telegram
from parser_bot import ParserAniDubLife, ParserAnimedubRu 
import asyncio


vkObj = VK('', '')
telegramObj = Telegram('dadadad')
parserObj_AnimedubRu = ParserAnimedubRu()
parserObj_AnimedubLife = ParserAniDubLife()


def messages_VK():
    """Принимает и отправляет сообщения
    """
    msg = vkObj.wait_message()
    flag = parserObj_AnimedubLife.search_on_site(msg['text'])
    if not(flag):
        text = 'По данному запросу ничего не найдено.'
        vkObj.send_message(text)
    else:
        parserObj_AnimedubLife.links_of_anime()
        parserObj_AnimedubLife.information_of_anime()
        text = f'{parserObj_AnimedubLife.info_of_anime_1}\nПриступить к просмотру: {parserObj_AnimedubLife.url_on_anime_1}'
        vkObj.send_message(text)
        if parserObj_AnimedubLife.url_on_anime_2 != None:
            vkObj.send_message('Чтобы показать следующий результат поиска введите ""') 

while True:
    messages_VK()

#while True:
#  Thread(target=send_response, args=(i,)).start()


if __name__ == '__main__':
    pass