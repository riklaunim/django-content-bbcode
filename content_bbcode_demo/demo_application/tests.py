from django.test import TestCase
from django.test import override_settings

from content_bbcode import cbcparser


class ParserTestCase(TestCase):
    def test_double_tag_is_parsed(self):
        text = 'foo [rk:b foo="bar"]bar[/rk:b] taz'
        expected = 'foo <b>bar</b> taz'
        result = self._parse_tags(text)
        self.assertEqual(expected, result)

    def test_double_tag_with_no_kwargs_is_parsed(self):
        text = 'foo [rk:b]bar[/rk:b] taz'
        expected = 'foo <b>bar</b> taz'
        result = self._parse_tags(text)
        self.assertEqual(expected, result)

    def test_multiple_double_tags_are_parsed_at_their_location(self):
        text = 'foo [rk:b foo="bar"]bar[/rk:b] taz [rk:b foo="bar"]lol[/rk:b]'
        expected = 'foo <b>bar</b> taz <b>lol</b>'
        result = self._parse_tags(text)
        self.assertEqual(expected, result)

    def test_single_tag_is_parsed(self):
        text = 'foo [rk:anchor href="http://www.google.pl"] bar'
        expected = 'foo <a href="http://www.google.pl">link</a> bar'
        result = self._parse_tags(text)
        self.assertEqual(expected, result)

    def test_single_tag_with_no_kwargs_is_parsed(self):
        text = 'foo [rk:test] bar'
        expected = 'foo TEST! bar'
        result = self._parse_tags(text)
        self.assertEqual(expected, result)

    def test_many_tags_parsing(self):
        text = 'foo [rk:anchor href="http://www.google.pl"] bar [rk:b foo="bar"]bar[/rk:b]'
        expected = 'foo <a href="http://www.google.pl">link</a> bar <b>bar</b>'
        result = self._parse_tags(text)
        self.assertEqual(expected, result)

    @override_settings(CONTENT_BBCODE_PREFIX='Anchesenamon')
    def test_custom_prefix_is_parsed(self):
        text = 'foo [Anchesenamon:test] bar'
        expected = 'foo TEST! bar'
        result = self._parse_tags(text)
        self.assertEqual(expected, result)

    @override_settings(CONTENT_BBCODE_PREFIX='Anchesenamon')
    def test_if_default_prefix_is_not_parsed_when_custom_given(self):
        text = 'foo [rk:test] bar'
        expected = 'foo [rk:test] bar'
        result = self._parse_tags(text)
        self.assertEqual(expected, result)

    @override_settings(CONTENT_BBCODE_PREFIX='Anchesenamon')
    def test_double_tag_with_prefix(self):
        text = 'foo [Anchesenamon:b]bar[/Anchesenamon:b] taz'
        expected = 'foo <b>bar</b> taz'
        result = self._parse_tags(text)
        self.assertEqual(expected, result)

    def _parse_tags(self, text):
        instance = cbcparser.ContentBBCodeParser()
        return instance.parse_tags(text)


class TemplateTagTestCase(TestCase):
    def test_integration(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)
        self.assertContains(response, '[rk:b]content bbcode example[/rk:b]')
        self.assertContains(response, '<b>content bbcode example</b>')
