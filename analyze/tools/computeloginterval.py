# -*- coding: utf-8 -*-
from analyze.methods.pair_stack import PairStack
from analyze.methods import log_helpers
from analyze.methods import string_utils
from analyze.methods import format_out


class ComputeLogInterval:

    def __init__(self, log_path, log_computed_repo, pattern="day time prior/tag:[tid:name] msg"):
        # log_computed
        self.log_path = log_path
        self.pattern = pattern
        self.log_computed_list = log_computed_repo
        self.compute_result = {}

    def compute_log_interval(self):
        with open(self.log_path) as log_file:
            self.compute_result = {}
            pair_stack = PairStack()
            for num, line in enumerate(log_file):
                in_pair = self.compose_pair(line)
                if not in_pair:
                    continue
                result_pair = pair_stack.push(in_pair, ComputeLogInterval.pair_diff)
                if result_pair:
                    self.statistics_compute_result(result_pair)
            return self.compute_result

    @staticmethod
    def pair_diff(pair_base, pair_compared):
        pattern = "hh:mm:ss.ms"
        return string_utils.str_time_long(pair_compared[2], pattern) - string_utils.str_time_long(pair_base[2], pattern)

    def compose_pair(self, origin_data):
        if not self.log_computed_list or len(self.log_computed_list) == 0:
            return None
        key = None
        state = None
        for log_off_pair in self.log_computed_list:
            key, state = log_off_pair.get_pair_identify(origin_data)
            if key and state:
                break
        if not key or not state:
            return None
        time = log_helpers.get_log_time(origin_data, self.pattern)
        if not time:
            return None
        return key, state, time

    def statistics_compute_result(self, result_pair):
        find_result = None
        for key, s_result in self.compute_result.items():
            if cmp(key, result_pair[0]) == 0:
                find_result = s_result
                break
        if not find_result:
            s_result = format_out.StatisticsResult(1, result_pair[1], result_pair[1], result_pair[1])
            self.compute_result.setdefault(result_pair[0], s_result)
        else:
            if result_pair[1] < find_result.min_time:
                find_result.min_time = result_pair[1]
            if result_pair[1] > find_result.max_time:
                find_result.max_time = result_pair[1]
            last_all_time = find_result.num * find_result.avg_time
            find_result.num += 1
            find_result.avg_time = (last_all_time + result_pair[1]) / find_result.num
