#!/usr/bin/python

from content_bbcode import loader
from content_bbcode import parsers


class ContentBBCodeParser(object):
    def __init__(self):
        self.tags = None

    def parse_tags(self, text):
        tags_definitions = self._get_tags()
        defined_parsers = [parsers.DoubleTagParser, parsers.SingleTagParser]
        for parser in defined_parsers:
            instance = parser(tags_definitions)
            text = instance.parse(text)
        return text

    def _get_tags(self):
        if self.tags is None:
            tag_loader = loader.LoadTags()
            self.tags = tag_loader.get_tags()
        return self.tags
