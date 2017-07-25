# -*- coding:utf-8 -*-
import log_helpers
import string_utils


def compute_logs_interval(pattern, base_log, compared_log):
    time1 = log_helpers.get_log_time(base_log, pattern)
    time2 = log_helpers.get_log_time(compared_log, pattern)
    if not time1 or not time2:
        return None
    time_ms1 = string_utils.str_time_long(time1)
    time_ms2 = string_utils.str_time_long(time2)
    return time_ms2-time_ms1

