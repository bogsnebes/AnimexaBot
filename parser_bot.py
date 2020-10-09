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
        """Поиск значения на сайте

        Args:
            text (str): Название аниме
        """
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
        """Поиск значения на сайте

        Args:
            text (str): Название аниме
        """
        anidub_post = 'https://anime.anidub.life/index.php?do=search'
        post = {
            'do': "search",
            'subaction': "search",
            'story': text
        }
        response = requests.post(anidub_post, data=post, headers=header).text
        # Обрабатываем ответ
        self.soup = bs4.BeautifulSoup(response, 'lxml')
        block = self.soup.find('div', id = 'main')
        test_if = str(block)
        if test_if.find("По Вашему запросу найдено") == -1:
            # Отправка сообщения о том, что запрос выстроен неправильно
            return False
        else:
            self.check_count_answers = block.find_all(attrs = {'class':'berrors'})
            self.check_count_answers = str(self.check_count_answers)
            self.check_count_answers = self.check_count_answers[44:-8]
            return True

    def links_of_anime(self):
        """Все ссылки на аниме с названиями"""
        block = self.soup.find_all(attrs = {'class':"th-in"})[1]
        a, b, c, self.url_on_anime_1, k = str(block).split('"', 4)
        if 'https://anime.anidub.life/videoblog/' in self.url_on_anime_1:
            self.url_on_anime_1 = None 
        try:
            block = self.soup.find_all(attrs = {'class':"th-in"})[3]
            a, b, c, self.url_on_anime_2, k = str(block).split('"', 4)
            if 'https://anime.anidub.life/videoblog/' in self.url_on_anime_2:
                self.url_on_anime_2 = None 
        except:
            self.url_on_anime_2 = None
            self.url_on_anime_3 = None
            return None
        try:
            block = self.soup.find_all(attrs = {'class':"th-in"})[5]
            a, b, c, self.url_on_anime_3, k = str(block).split('"', 4)
            if 'https://anime.anidub.life/videoblog/' in self.url_on_anime_3:
                self.url_on_anime_3 = None 
        except:
            self.url_on_anime_3 = None
            return None

    def information_of_anime(self):
        """Информация о аниме с его ссылкой"""
        response = requests.get(self.url_on_anime_1, headers = header)
        soup = bs4.BeautifulSoup(response, 'lxml')
        block = soup.find(attrs = {'meta property':'og:title'})

class ParserAnimedubRu(Parser):
    """Парсер для сайта https://animedub.ru/"""
    def search_on_site(self, text):
        """Поиск значения на сайте

        Args:
            text (str): Название аниме
        """
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
        block = self.soup.find('div', id = 'dle-content')
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