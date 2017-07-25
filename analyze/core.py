# -*- coding: utf-8 -*-
from analyze.methods import log_helpers
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
            results = []
            tag_tools = tagtools.TestTools(self.pattern, self.scan_config)
            for line in log_file:
                if not log_helpers.check_log_line_from_main(line, self.pattern):
                    continue
                parse_result = tag_tools.parse_log_line(line)
                if parse_result:
                    results.append(tag_tools.m_tag_list)
                    tag_tools = tagtools.TestTools(self.pattern, self.scan_config)
            return results

