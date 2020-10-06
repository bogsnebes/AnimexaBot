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
        self.text = text[text]
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
        print('')
        if 'К сожалению, поиск по сайту не дал никаких результатов. Попробуйте изменить или сократить Ваш запрос.' in block:
            #Отправка сообщения о том, что запрос выстроен неправильно
            print('Запрос неверен')
            return False
        else:
            check_count_answers = block.find_all(attrs = {'class':'berrors'})
            check_count_answers = str(check_count_answers)
            check_count_answers = check_count_answers[44:-8]
            return check_count_answers
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
    def wait_message(self):
        """Бот ждет сообщения от пользователя. Получает данные типа dict"""
        for event in self.longpoll.listen():
            self.msg = {}
            if event == VkBotEventType.MESSAGE_NEW:
                self.msg['text'] = event.obj.text() # Текст сообщения
                self.msg['user_id'] = str(event.obj.from_id()) # User, который отправил сообщения
                self.msg['random_id'] = r.randint(-2147483648,2147483647)
                return self.msg
    def send_message(self, text):
        """Отправка сообщения пользователю"""
        self.msg.pop('text', None)
        self.vk.method('messages.send', self.msg, text)


vkObj = VK('87dab7a794019fa7ff9237a2ab5a1fce32e760291c44eddb8fdf3eaf179270a88e38eb820b65af2a902c2', '199231862')
telegramObj = Telegram()
parserObj = Parser()


data_user = vkObj.wait_message()
data_search = parserObj.search_on_site(data_user)
vkObj.send_message(data_search)


if '__init__' == "__main__":
    pass