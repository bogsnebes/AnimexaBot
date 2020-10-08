import vk_api
import telegram
import requests
import bs4
import fake_useragent
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random as r


useragent = fake_useragent.UserAgent().random
header = {
    'useragent': useragent
    }

class Parser():
    def search_on_site(self, text):
        """Поиск значения на сайте"""
        self.text = text
        print(self.text)
        anidub_post = 'https://anime.anidub.life/index.php?do=search'
        post = {
            'do': "search",
            'subaction': "search",
            'story': self.text
        }
        response = requests.post(anidub_post, data=post, headers=header).text
        # Обрабатываем ответ
        self.soup = bs4.BeautifulSoup(response, 'lxml')
        block = self.soup.find('div', id = 'main')
        print(block)
        if 'К сожалению, поиск по сайту не дал никаких результатов. Попробуйте изменить или сократить Ваш запрос.' in block:
            #Отправка сообщения о том, что запрос выстроен неправильно
            print('Запрос неверен')
            return False
        else:
            self.check_count_answers = block.find_all(attrs = {'class':'berrors'})
            self.check_count_answers = str(self.check_count_answers)
            self.check_count_answers = self.check_count_answers[44:-8]
            return True
    def information_of_anime(self):
        """Информация о аниме с его ссылкой"""
        # Ссылка на аниме
        block = self.soup.find(attrs = {'class':"th-in"})
        a, b, c, d, k = str(block).split('"', 4)
        return(d)
    def links_of_anime(self):
        """Все ссылки на аниме с названиями""" 
        pass
class Telegram():
    def __init__(self, API_KEY):
        self.API_KEY = API_KEY


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
            print('Hello nigga')
            print(event)
            self.msg = {}
            if 'message_new' in voprosi:
                print(type(event))
                self.msg['text'] = event.obj['message']['text'] # Текст сообщения
                print(self.msg['text'])
                self.msg['user_id'] = str(event.obj['message']['from_id']) # User, который отправил сообщения
                self.msg['random_id'] = r.randint(-2147483648,2147483647)
                return self.msg
    def send_message(self, text):
        """Отправка сообщения пользователю"""
        self.msg.pop('text', None)
        self.msg['message'] = text
        print(self.msg)
        self.vk.method('messages.send', self.msg)


vkObj = VK('6cb02efc792b6ab73f5128fc0a2ff825456cae8daa81fc22e9b747381d41b6287e0877529ba6106ce76e8', '199231862')
#telegramObj = Telegram()
parserObj = Parser()

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


if '__init__' == "__main__":
    pass