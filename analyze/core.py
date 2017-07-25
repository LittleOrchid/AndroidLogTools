# -*- coding: utf-8 -*-
from analyze.methods import helpers
from analyze.methods import tagtools
from config import Config


class ScanLogTool:
    def __init__(self, log_path, activity="com.alipay.mobile.scan.as.main.MainCaptureActivity",
                 pattern="day time prior/tag:[tid:name] msg"):
        self.log_path = log_path
        self.activity = activity
        self.pattern = pattern
        self.scan_config = Config(activity)

    def scan_log_analysis(self):
        with open(self.log_path) as log_file:
            tag_sets = tagtools.TestTools(self.pattern)
            for line in log_file:
                if not helpers.check_log_line_from_main(line, self.pattern):
                    continue
                tag_sets.parse_log_line(line)
            return tag_sets.m_tag_list

    # def scan_analysis_main_thread(self, origin_data):
    #     activity_start_features = self.scan_config
    #     activity_end_log =
    #     if not origin_data:
    #         return "NONE"
    #     elif string_utils.string_contains_features(origin_data, activity_start_features):
    #         return "BLOCK_BEGIN"
    #     elif origin_data.find(activity_end_log) >= 0:
    #         return "BLOCK_END"
    #     else:
    #         return "NORM"

