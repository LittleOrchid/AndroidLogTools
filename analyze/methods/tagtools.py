# -*- coding: utf-8 -*-
import log_helpers
import string_utils
from analyze.config import Config
from format_out import PairList


class TestTools:

    def __init__(self, pattern, config):
        self.m_tag_list = PairList()
        self.pattern = pattern
        self.config = config
        self.cur_phase = Config.NONE
        self.cur_phase_list = []

    def parse_log_line(self, origin_data):
        if not origin_data:
            return False
        phase_code = self.log_appear_phase(origin_data)
        if cmp(self.cur_phase, Config.OUT) == 0:
            self.m_tag_list.append((Config.OUT, []))
            return True
        if cmp(phase_code, Config.NONE) == 0:
            return False
        if cmp(phase_code, Config.NORM) != 0:
            if cmp(self.cur_phase, Config.NONE) != 0:
                self.m_tag_list.append((self.cur_phase, self.cur_phase_list))
            self.cur_phase = phase_code
            self.cur_phase_list = []
        tag = log_helpers.get_tag(origin_data, self.pattern)
        if not tag:
            return False
        self.cur_phase_list.append(tag)
        return False

    def log_appear_phase(self, origin_data):
        # 判断日志出现的phase阶段
        self.config.activity
        if not origin_data:
            return Config.NONE
        elif string_utils.string_contains_features(origin_data, self.config.scan_lifecycle_tag[Config.IN]):
            return Config.IN
        elif string_utils.string_contains_features(origin_data, self.config.scan_lifecycle_tag[Config.ON_CREATE]):
            return Config.ON_CREATE
        elif string_utils.string_contains_features(origin_data, self.config.scan_lifecycle_tag[Config.ON_RESUME]):
            return Config.ON_RESUME
        elif string_utils.string_contains_features(origin_data, self.config.scan_lifecycle_tag[Config.ON_PAUSE]):
            return Config.ON_PAUSE
        elif string_utils.string_contains_features(origin_data, self.config.scan_lifecycle_tag[Config.OUT]):
            return Config.OUT
        else:
            return Config.NORM

