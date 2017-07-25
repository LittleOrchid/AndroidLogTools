# -*- coding: utf-8 -*-
import helpers
import string_utils
from analyze.config import Config


class TestTools:

    def __init__(self, pattern, config):
        self.m_tag_list = {Config.IN: [], Config.ON_CREATE: [], Config.ON_RESUME: [],
                           Config.ON_PAUSE: [], Config.ON_DESTROY: []}
        self.pattern = pattern
        self.config = config
        self.cur_phase = Config.NONE

    def parse_log_line(self, origin_data):
        if not origin_data:
            return
        phase_code = self.log_appear_phase(origin_data)
        if cmp(phase_code, Config.NONE) != 0 and cmp(phase_code, Config.NORM) != 0:
            self.cur_phase = phase_code
        tag = helpers.get_tag(origin_data, self.pattern)
        if not tag or cmp(self.cur_phase, Config.NONE) == 0 or cmp(self.cur_phase, Config.OUT) == 0:
            return
        self.m_tag_list[self.cur_phase].append(tag)

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

