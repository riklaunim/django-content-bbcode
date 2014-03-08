import sys

from content_bbcode.settings import TAGS_SCAN_MODULES


class LoadTags(object):
    def __init__(self):
        self.tags = None

    def find(self):
        taglist = {}
        for app_name, module_name in TAGS_SCAN_MODULES.items():
            try:
                __import__(module_name)
                tags = sys.modules[module_name]
                if hasattr(tags, 'registered_tags'):
                    taglist.update(tags.registered_tags)
            except ImportError:
                pass
        return taglist

    def get_tags(self):
        if self.tags is None:
            self.tags = self.find()
        return self.tags
