import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random as r


class VK():
    def __init__(self, API_KEY = None, ID = None):
        """Данные API сообщества и его ID"""
        self.vk = vk_api.VkApi(token = API_KEY)
        self.longpoll = VkBotLongPoll(self.vk, ID)
        print('Whats up ?')
    def wait_message(self):
        """Бот ждет сообщения от пользователя. Получает данные типа dict"""
        for event in self.longpoll.listen():
            voprosi = str(event)
            self.msg = {}
            if 'message_new' in voprosi:
                self.msg['text'] = event.obj['message']['text'] # Текст сообщения
                self.msg['user_id'] = str(event.obj['message']['from_id']) # User, который отправил сообщения
                self.msg['random_id'] = r.randint(-2147483648,2147483647)
                return self.msg
    def send_message(self, text):
        """Отправка сообщения пользователю"""
        self.msg.pop('text', None)
        self.msg['message'] = text
        print(self.msg)
        self.vk.method('messages.send', self.msg)


if __name__ == '__main__':
    pass