# -*- coding: utf-8 -*-
import helpers


class TestTools:

    def __init__(self, pattern):
        self.m_tag_list = set([])
        self.pattern = pattern

    def parse_log_line(self, origin_data):
        if not origin_data:
            return
        tag = helpers.get_tag(origin_data, self.pattern)
        if not tag:
            return
        self.m_tag_list.add(tag)

