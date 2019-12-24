import unittest

from rusmarkup import rusmarkup2html, tags_map


class TestStringMethods(unittest.TestCase):

    def setUp(self) -> None:
        self.markupper = rusmarkup2html(tags_map)

    def test_header(self):
        self.assertEqual(self.markupper("(ЗАГОЛОВОК)Это заголовок(ЗАГОЛОВОК)"),
                         '<h3 class="rusmarkup-subheader">Это заголовок</h3>')

    def test_image(self):
        self.assertEqual(self.markupper("(ССЫЛКА)https://cdn.pixabay.com/photo/2019/12/13/08/27/snow-4692469_960_720.jpg занесло снегом(ссылка)"),
                         '<img class="rusmarkup-image" src="https://cdn.pixabay.com/photo/2019/12/13/08/27/snow-4692469_960_720.jpg" alt="занесло снегом">')

    def test_link(self):
        self.assertEqual(self.markupper("(ССЫЛКА)https://korablik-fond.ru/ Кораблик(ССЫЛКА)"),
                         '<a class="rusmarkup-link"  href="https://korablik-fond.ru/">Кораблик</a>')

    def test_video(self):
        self.assertEqual(self.markupper("(ССЫЛКА)https://www.videvo.net/videvo_files/converted/2017_08/preview/170724_15_Setangibeach.mp486212.webm пальмы(ССЫЛКА)"),
                         '<video class="rusmarkup-video" width="480" controls src="https://www.videvo.net/videvo_files/converted/2017_08/preview/170724_15_Setangibeach.mp486212.webm"><a href="https://www.videvo.net/videvo_files/converted/2017_08/preview/170724_15_Setangibeach.mp486212.webm">пальмы</a></video>')

    def test_audio(self):
        self.assertEqual(self.markupper("(ССЫЛКА)https://files.freemusicarchive.org/storage-freemusicarchive-org/music/Music_for_Video/Blue_Dot_Sessions/RadioPink/Blue_Dot_Sessions_-_Slow_Rollout.mp3 какая-то аудиодорожка(ССЫЛКА)"),
                         '<audio class="rusmarkup-audio" width="480" controls src="https://files.freemusicarchive.org/storage-freemusicarchive-org/music/Music_for_Video/Blue_Dot_Sessions/RadioPink/Blue_Dot_Sessions_-_Slow_Rollout.mp3"><a href="https://files.freemusicarchive.org/storage-freemusicarchive-org/music/Music_for_Video/Blue_Dot_Sessions/RadioPink/Blue_Dot_Sessions_-_Slow_Rollout.mp3">какая-то аудиодорожка</a></audio>')

    def test_youtube(self):
        self.assertEqual(self.markupper("(ССЫЛКА)https://www.youtube.com/watch?v=UGuqxiKxNDE фонд Кораблик(ССЫЛКА)"),
                         '<div class="rusmarkup-youtube" data-id="UGuqxiKxNDE"></div>')

    def test_warning(self):
        self.assertEqual(self.markupper("(ПРЕДУПРЕЖДЕНИЕ)это предупреждение(ПРЕДУПРЕЖДЕНИЕ)"),
                         '<p class="rusmarkup-warning">это предупреждение</p>')

    def test_tip(self):
        self.assertEqual(self.markupper("(СОВЕТ)это совет(СОВЕТ)"),
                         '<p class="rusmarkup-tip">это совет</p>')

    def test_blockquote(self):
        self.assertEqual(self.markupper("(ЦИТАТА)это цитата(ЦИТАТА)"),
                         '<blockquote class="rusmarkup-quote">это цитата</blockquote>')

    def test_list(self):
        items = "(список)Позиция 1\n    Позиция 1.1\n    Позиция 1.2\nПозиция 2(список)"
        self.assertEqual(self.markupper(items),
                         '<ol class="rusmarkup-list"><li>Позиция 1<ol class="rusmarkup-list"><li>Позиция 1.1</li><li>Позиция 1.2</li></ol></li><li>Позиция 2</li></ol>')

    def test_strong(self):
        self.assertEqual(self.markupper("(жирный)полужирный(жирный)"),
                         '<strong class="rusmarkup-strong">полужирный</strong>')

    def test_em(self):
        self.assertEqual(self.markupper("(курсив)это курсивом(курсив)"),
                         '<em class="rusmarkup-emphasized">это курсивом</em>')

    def test_sup(self):
        self.assertEqual(self.markupper("(верхнийрегистр) текст в верхнем регистре (верхнийрегистр)"),
                         '<sup> текст в верхнем регистре </sup>')

    def test_sub(self):
        self.assertEqual(self.markupper("(нижнийрегистр) текст в нижнем регистре(нижнийрегистр)"),
                         '<sub> текст в нижнем регистре</sub>')

    def test_nested_tags(self):
        self.assertEqual(self.markupper("(жирный)(курсив)это жирным курсивом(курсив)(жирный)"),
                         '<strong class="rusmarkup-strong"><em class="rusmarkup-emphasized">это жирным курсивом</em></strong>')

    def test_remove_tags(self):
        cleared = self.markupper("(жирный)(курсив)это жирным курсивом(курсив)(жирный)")
        self.assertTrue('(жирный)' not in cleared)
        self.assertTrue('(курсив)' not in cleared)


if __name__ == '__main__':
    unittest.main()
