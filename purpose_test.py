from parser_bot import ParserAniDubLife, ParserAnimedubRu 
from vk import VK
from telegram_bot import Telegram


vkObj = VK('', '')
telegramObj = Telegram('')
parserObj_AnimedubRu = ParserAnimedubRu()
parserObj_AnimedubLife = ParserAniDubLife()


parserObj_AnimedubLife.links_of_anime()