# -*- coding:utf-8 -*-


class PairList:
    def __init__(self):
        self.list = []

    def length(self):
        return len(self.list)

    def append(self, pair):
        self.list.append(pair)

    def contains(self, key):
        find_result = False
        for pair in self.list:
            if cmp(pair.first, key) == 0:
                find_result = True
                break
        return find_result

    def get(self, key):
        result = None
        for pair in self.list:
            if cmp(pair.first, key) == 0:
                result = pair.second
        return result

    def get_all_results(self):
        return self.list

    def format_out(self, prefix='', step_num=0):
        format_out(self.list, prefix, step_num)


def format_out(result, prefix='', step_num=0):
    if isinstance(result, list):
        format_list_out(result, prefix, step_num)
    elif isinstance(result, PairList):
        result.format_out(prefix, step_num)
    elif isinstance(result, tuple):
        format_tuple_out(result, prefix, step_num)
    elif isinstance(result, str):
        format_str_out(result, prefix, step_num)


def format_list_out(result_list, prefix='', step_num=0):
    if not result_list or len(result_list) == 0:
        return
    for item in result_list:
        format_out(item, prefix, step_num+1)


def format_tuple_out(result_tuple, prefix='', step_num=0):
    if not result_tuple or len(result_tuple) == 0:
        return
    tmp_step_num = step_num
    for item in result_tuple:
        tmp_step_num += 1
        format_out(item, prefix, tmp_step_num)


def format_str_out(result_str, prefix='', step_num=0):
    if not result_str:
        return
    for index in range(0, step_num):
        prefix += '\t'
    print prefix+result_str


def format_map_list_out(result_set_list, key_order_list=None):
    if not result_set_list or len(result_set_list) == 0:
        return
    if not key_order_list:
        for key, item_list in result_set_list.items():
            print(key)
            format_list_out(item_list, 1)
    else:
        for key in key_order_list:
            print(key)
            format_list_out(result_set_list[key], 1)

