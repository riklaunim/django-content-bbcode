#!/usr/bin/python
from content_bbcode import cbcparser
from django import template

register = template.Library()


def parse_content_bbcode(value):
    if value:
        instance = cbcparser.ContentBBCodeParser()
        return instance.parse_tags(value)
    else:
        return u''

register.filter('parse_content_bbcode', parse_content_bbcode)
