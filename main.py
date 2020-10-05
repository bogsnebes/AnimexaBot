import vk_api
import telegram
import requests
import bs4
import fake_useragent
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random as r

useragent = fake_useragent.UserAgent().random


def Parser():
    site_1 = ''
    site_2 = ''


class Telegram():
    def __init__(self, API_KEY):
        self.API_KEY = API_KEY
    

class VK():
    def __init__(self, API_KEY = None, ID = None):
        """Данные API сообщества и его ID"""
        self.API_KEY = API_KEY
        self.ID = ID
        vk_group = ID, API_KEY
        vk_api.VkApi(token = vk_group[1])
        longpoll = VkBotLongPoll(vk,vk_group[0])
    def wait_message(self):
        """Бот ждет сообщения от пользователя. Получает данные типа dict"""
        for event in longpoll.listen():
            msg = {}
            if event == VkBotEventType.MESSAGE_NEW:
                msg['text'] = event.obj.text() # Текст сообщения
                msg['user_id'] = str(event.obj.from_id()) # User, который отправил сообщения
                msg['random_id'] = r.randint(-2147483648,2147483647)
    def send_message():
        """Отправка сообщения пользователю"""
        if #adada
            vk.method('messages.send', msg)


if __init__ == "__main__":
    pass