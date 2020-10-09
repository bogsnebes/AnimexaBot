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
        def info_about_one_url(url):
            """Берет ссылку на аниме страницу, после чего парсит её и выводит всю информацию

            Args:
                url (str): можно вставить любую ссылку на аниме тайтл

            Returns:
                [str]: возвращает название и полное описание аниме
            """
            response = requests.get(url, headers = header).text
            soup = bs4.BeautifulSoup(response, 'lxml')
            block = soup.find('meta', attrs = {'property':'og:title'})
            self.name = str(block)
            self.name = self.name[15:-23]
            description_block = soup.find('div', attrs = {'class':'fdesc clr full-text clearfix'})
            for_for = str(description_block)
            flag = False
            self.description = ''
            for i in for_for:
                if i == '<':
                    flag = True
                elif i == '>':
                    flag = False
                if flag or i == '>':
                    continue
                else:
                    self.description += i
            def clear_pars(number_block):
                """Очистка значений парса от мусора

                Args:
                    number_block[int]: строка чтения find_all
                
                Returns:
                    [str]: чистое значение строки без разметки HTML
                """
                block = soup.find_all('li', attrs = {'class':'short-info'})[number_block]
                for_for = str(block)
                flag = False
                category = ''
                for i in for_for:
                    if i == '<':
                        flag = True
                    elif i == '>':
                        flag = False
                    if flag or i == '>':
                        continue
                    else:
                        category += i
                return category
            self.genre = clear_pars(0)
            self.count = clear_pars(1)
            self.start = clear_pars(2)
            self.auther = clear_pars(3)
            self.producer = clear_pars(4)
            self.studio = clear_pars(5)
            self.voice_acting = clear_pars(6)
            self.taming = clear_pars(7)
            info_of_anime = f'{self.name}\n\n{self.genre}\n{self.count}\n{self.start}\n{self.auther}\n{self.producer}\n{self.studio}\n{self.voice_acting}\n{self.taming}\n\nОписание\n{self.description}'
            return info_of_anime
        self.info_of_anime_1 = info_about_one_url(self.url_on_anime_1)
        if self.url_on_anime_2 != None:
            self.info_of_anime_2 = info_about_one_url(self.url_on_anime_2)
            if self.url_on_anime_3 != None:
                self.info_of_anime_3 = info_about_one_url(self.url_on_anime_3)


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