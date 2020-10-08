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
        result = self.parserObj_AnimedubLife.search_on_site('dwa')
        self.assertFalse(result)
        result = self.parserObj_AnimedubLife.search_on_site('Убийца гоблинов')
        self.assertTrue(result)
    def test_search_on_site_AnimeDubRu(self):
        """Проверка работоспособности парсера на сайте AnimeDubRu"""
        result = self.parserObj_AnimedubRu.search_on_site('d')
        self.assertFalse(result)
        result = self.parserObj_AnimedubRu.search_on_site('dwa')
        self.assertFalse(result)
        result = self.parserObj_AnimedubRu.search_on_site('Убийца гоблинов')
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()