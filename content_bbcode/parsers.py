from re import findall

from django.conf import settings


class BaseTagParser(object):
    regexp = NotImplementedError

    def __init__(self, tags_definitions):
        self.definitions = tags_definitions
        self.parsed_data = {}

    def parse(self, text):
        tags_in_text = findall(self.regexp.format(PREFIX=get_prefix()), text)

        for tag_args in tags_in_text:
            self._parse_tag_occurrence(*tag_args)

        for tag_name in self.parsed_data:
            if tag_name in self.definitions:
                text = self.definitions[tag_name](self.parsed_data[tag_name], text)
        return text

    def _parse_tag_occurrence(self, *args, **kwargs):
        raise NotImplementedError

    @staticmethod
    def _parse_kwargs(tag_kwargs):
        parts = tag_kwargs.split('" ')
        kwargs = {}
        for attr in parts:
            attr = attr.split('=')
            if len(attr) > 1:
                val = attr[1]
                if val[-1] != '"':
                    attr[1] = val[1:]
                else:
                    attr[1] = val[1:-1]
                kwargs[attr[0]] = attr[1]
        return kwargs

    @staticmethod
    def _get_tag_string(*args):
        raise NotImplementedError


class DoubleTagParser(BaseTagParser):
    regexp = r'(?xs)\[\s*{PREFIX}:([a-z0-9\-]*)(.*?)\](.*?)\[(?=\s*/{PREFIX})\s*/{PREFIX}:(\1)\s*\]'''

    @staticmethod
    def _get_tag_string(tag_name, tag_kwargs, tag_text):
        prefix = get_prefix()
        if tag_kwargs:
            return '[' + prefix + ':' + tag_name + ' ' + tag_kwargs + ']' + tag_text + '[/' + prefix + ':' + tag_name + ']'
        return '[' + prefix + ':' + tag_name + ']' + tag_text + '[/' + prefix + ':' + tag_name + ']'

    def _parse_tag_occurrence(self, tag_name, tag_kwargs, tag_text, _):
        tag_kwargs = tag_kwargs.strip()
        tag_instance = dict(attributes=self._parse_kwargs(tag_kwargs))
        tag_instance['code'] = tag_text
        tag_instance['tag'] = self._get_tag_string(tag_name, tag_kwargs, tag_text)
        if not tag_name in self.parsed_data:
            self.parsed_data[tag_name] = list()
        self.parsed_data[tag_name].append(tag_instance)


class SingleTagParser(BaseTagParser):
    regexp = r'\[{PREFIX}:([a-z_0-9\-]*)(.*?)\]'

    @staticmethod
    def _get_tag_string(tag_name, tag_kwargs):
        prefix = get_prefix()
        if tag_kwargs:
            return '[' + prefix + ':' + tag_name + ' ' + tag_kwargs + ']'
        return '[' + prefix + ':' + tag_name + ']'

    def _parse_tag_occurrence(self, tag_name, tag_kwargs):
        tag_kwargs = tag_kwargs.strip()
        tag_instance = dict(attributes=self._parse_kwargs(tag_kwargs))
        tag_instance['tag'] = self._get_tag_string(tag_name, tag_kwargs)
        if not tag_name in self.parsed_data:
            self.parsed_data[tag_name] = list()
        self.parsed_data[tag_name].append(tag_instance)


def get_prefix():
    return getattr(settings, 'CONTENT_BBCODE_PREFIX', 'rk')
