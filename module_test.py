import unittest
from parser_bot import ParserAniDubLife, ParserAnimedubRu 
from vk import VK
from telegram_bot import Telegram

class Tests(unittest.TestCase):
    vkObj = VK('6cb02efc792b6ab73f5128fc0a2ff825456cae8daa81fc22e9b747381d41b6287e0877529ba6106ce76e8', '199231862')
    telegramObj = Telegram('awdawdawd')
    parserObj_AnimedubRu = ParserAnimedubRu()
    parserObj_AnimedubLife = ParserAniDubLife()
    maxDiff = None
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
        self.parserObj_AnimedubLife.search_on_site('Убийца гоблинов')
        self.parserObj_AnimedubLife.links_of_anime()
        url_1 = 'https://anime.anidub.life/anime_movie/11281-ubijca-goblinov-goblin-slayer-goblins-crown.html'
        self.assertEqual(self.parserObj_AnimedubLife.url_on_anime_1, url_1)
        self.assertEqual(self.parserObj_AnimedubLife.url_on_anime_2, None)
        self.assertEqual(self.parserObj_AnimedubLife.url_on_anime_3, None)

        self.parserObj_AnimedubLife.search_on_site('One punch man')
        self.parserObj_AnimedubLife.links_of_anime()
        url_1 = 'https://anime.anidub.life/anime/full/10771-vanpanchmen-tv-2-one-punch-man-tv-2-aprel-2019.html'
        url_2 = 'https://anime.anidub.life/anime/full/9447-vanpanchmen-one-punch-man-01-iz-12.html'
        url_3 = 'https://anime.anidub.life/anime_ova/9560-vanpanchmen-one-punch-man-ova.html'
        self.assertEqual(self.parserObj_AnimedubLife.url_on_anime_1, url_1)
        self.assertEqual(self.parserObj_AnimedubLife.url_on_anime_2, url_2)
        self.assertEqual(self.parserObj_AnimedubLife.url_on_anime_3, url_3)
    def test_information_of_anime_AnimeDubLife(self):
        """Проверка отображения информации об аниме"""
        self.parserObj_AnimedubLife.search_on_site('One punch man')
        self.parserObj_AnimedubLife.links_of_anime()
        self.parserObj_AnimedubLife.information_of_anime()
        info_1 = """\
        Ванпанчмен Сезон 2 ТВ-2 / One-Punch Man TV-2 12 из 12\n\nЖанр: экшен, фантастика, комедия, пародия, супер сила, сверхъестественное, сейнен\n
        Количество серий: 12\nНачало показа: c 10.04.2019 по 03.07.2019\nАвтор оригинала: ONE\n
        Режиссер: Сакурай Тикара\nСтудия: J.C.Staff\nОзвучивание: JAM\nТайминг: Lonty\n\nОписание\n
        Он вернулся! Наш любимый лысый хохмач снова натирает лысину и перчатки гуталином, дабы "блистать" во всей красе и по царски поджигать вражеские седалища!
        Сайтама - в прошлом безработный лузер по жизни, со сверхнизкой самооценкой и склонностью к самоубийству. После отказа идти "против системы" и на основе детской мечты, он забивает на попытки трудоустроиться, начинает качаться и становится мега-супергероем, выносящим всех с одной плюшки.
        Спустя определенное время после отражения вторжения "Тёмной Материи" на Земле наступило относительное затишье (Ну да, в среду "Всемирный Потоп", в четверг "Восстание Зомби-Жирафов"... Подумаешь...), но это не навсегда. Появляется предсказание, по которому через полгода землю снова ждёт полный абзац. Пока Земляне мажут ласты клеем, а "Ассоциация Героев" ломает систему и вербует суперзлодеев, Сайтама и Генос как всегда пинают... Кхм, в попутных поисках приключений на соседнее место.
        В этот момент появляется новый суперзлодей, пославший весь мир и забивший на спасение человечества, роняет весь А-класс на лопатки и объявляет себя сильнейшим на планете. Догадайтесь, кто за такое ЧСВ принесёт ответное огребалити..."""
        info_2 = 'Ванпанчмен [12 из 12 + SP 06 из 06]\nЖанр: боевик, фэнтези, приключения, повседневность, комедия, фантастика\nКоличество серий: 12\nНачало показа: c 05.10.2015 по 21.12.2015\nАвтор оригинала: ONE\nРежиссер: Нацумэ Синго\nСтудия: Madhouse Studios\nПеревод: AleX_MytH, BO3DYX, Reaper, Anku, mutagenb\nОзвучивание: JAM\nТайминг: SunRiZ, Sakuragi_R\n\nОписание\nИстория повествует о юноше по имени Саитама, который живет в мире, иронично похожем на наш. Ему 25, он лыс и прекрасен, к тому же, силен настолько, что с одного удара аннигилирует все опасности для человечества. Он ищет себя на нелегком жизненном пути, попутно раздавая подзатыльники монстрам и злодеям.'
        self.assertEqual(self.parserObj_AnimedubLife.info_of_anime_1, info_1)
        self.assertEqual(self.parserObj_AnimedubLife.info_of_anime_2, info_2)

if __name__ == '__main__':
    unittest.main()