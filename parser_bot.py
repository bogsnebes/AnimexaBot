import requests
import bs4
import fake_useragent
import string

# Создания фейк-юзер агента
useragent = fake_useragent.UserAgent().random
header = {
    'useragent': useragent
    }


class Parser():
    """Интерфейс парсера сайта"""
    def search_on_site(self, text):
        """Поиск значения на сайте"""
        pass
    def information_of_anime(self):
        """Информация о аниме с его ссылкой"""
        pass
    def links_of_anime(self):
        """Все ссылки на аниме с названиями""" 
        pass


class ParserAniDubLife(Parser):
    """Парсер для сайта https://anime.anidub.life/"""
    def search_on_site(self, text):
        """Поиск значения на сайте"""
        self.text = text
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
        test_if = str(block)
        f = open('text.txt', 'w')
        f.write(test_if)
        f.close()
        if test_if.find("По Вашему запросу найдено") == -1:
            # Отправка сообщения о том, что запрос выстроен неправильно
            return False
        else:
            self.check_count_answers = block.find_all(attrs = {'class':'berrors'})
            self.check_count_answers = str(self.check_count_answers)
            self.check_count_answers = self.check_count_answers[44:-8]
            return True

    def information_of_anime(self):
        """Информация о аниме с его ссылкой"""
        block = self.soup.find(attrs = {'class':"th-in"})
        a, b, c, url_on_anime, k = str(block).split('"', 4)
        return url_on_anime # Ссылка на аниме


class ParserAnimedubRu(Parser):
    """Парсер для сайта https://animedub.ru/"""
    def search_on_site(self, text):
        self.text = text
        anidub_post = 'https://animedub.ru/index.php?do=search'
        post = {
            'do': "search",
            'subaction': "search",
            'story': self.text
        }
        response = requests.post(anidub_post, data=post, headers=header).text
        # Обрабатываем ответ
        self.soup = bs4.BeautifulSoup(response, 'lxml')
        block = block.find_all(attrs = {'class':'berrors'})
        test_if = str(block)
        if test_if.find("По Вашему запросу найдено") == -1:
            # Отправка сообщения о том, что запрос выстроен неправильно
            return False
        else:
            # Отправка сообщения о том, что запрос правильный
            self.check_count_answers = block.find_all(attrs = {'class':'berrors'})
            self.check_count_answers = str(self.check_count_answers)
            self.check_count_answers = self.check_count_answers[44:-8]
            return True


if __name__ == '__main__':
    pass