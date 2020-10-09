import unittest
from parser_bot import ParserAniDubLife, ParserAnimedubRu 
from vk import VK
from telegram_bot import Telegram

class Tests(unittest.TestCase):
    vkObj = VK('6cb02efc792b6ab73f5128fc0a2ff825456cae8daa81fc22e9b747381d41b6287e0877529ba6106ce76e8', '199231862')
    telegramObj = Telegram('awdawdawd')
    parserObj_AnimedubRu = ParserAnimedubRu()
    parserObj_AnimedubLife = ParserAniDubLife()
    def test_search_on_site_AnimeDubLife(self):
        """Проверка работоспособности парсера на сайте AnimeDubLife"""
        result = self.parserObj_AnimedubLife.search_on_site('d')
        self.assertFalse(result)
        result = self.parserObj_AnimedubLife.search_on_site('dawdsdafasda')
        self.assertFalse(result)
        result = self.parserObj_AnimedubLife.search_on_site('Убийца гоблинов')
        self.assertTrue(result)
    def test_search_on_site_AnimeDubRu(self):
        """Проверка работоспособности парсера на сайте AnimeDubRu"""
        result = self.parserObj_AnimedubRu.search_on_site('d')
        self.assertFalse(result)
        result = self.parserObj_AnimedubRu.search_on_site('dawdsdafasda')
        self.assertFalse(result)
        result = self.parserObj_AnimedubRu.search_on_site('Убийца гоблинов')
        self.assertTrue(result)
    def test_link_of_anime_AnimeDubLife(self):
        """Проверка вылавливания ссылки на страницу с анимой"""
        self.parserObj_AnimedubRu.search_on_site('Убийца гоблинов')
        self.parserObj_AnimedubLife.links_of_anime()
        url_1 = 'https://anime.anidub.life/anime_movie/11281-ubijca-goblinov-goblin-slayer-goblins-crown.html'
        url_2 = 'https://anime.anidub.life/videoblog/10620-chto-pokazali-a-treylere-anime-ubiyca-goblinov-goblin-slayer.html'
        self.assertEqual(self.parserObj_AnimedubLife.url_on_anime_1, url_1)
        self.assertEqual(self.parserObj_AnimedubLife.url_on_anime_2, url_2)
        self.assertEqual(self.parserObj_AnimedubLife.url_on_anime_3, None)

        self.parserObj_AnimedubRu.search_on_site('One punch man')
        self.parserObj_AnimedubLife.links_of_anime()
        url_1 = 'https://anime.anidub.life/anime/full/10771-vanpanchmen-tv-2-one-punch-man-tv-2-aprel-2019.html'
        url_2 = 'https://anime.anidub.life/anime/full/9447-vanpanchmen-one-punch-man-01-iz-12.html'
        url_3 = 'https://anime.anidub.life/anime_ova/9560-vanpanchmen-one-punch-man-ova.html'
        self.assertEqual(self.parserObj_AnimedubLife.url_on_anime_1, url_1)
        self.assertEqual(self.parserObj_AnimedubLife.url_on_anime_2, url_2)
        self.assertEqual(self.parserObj_AnimedubLife.url_on_anime_3, url_3)


if __name__ == '__main__':
    unittest.main()