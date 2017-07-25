# -*- coding:utf-8 -*-
from string_utils import split_string_character
from string_utils import split_string_character_delimiter


def check_log_line_from_main(origin_line, pattern):
    res_thread_name = get_thread_name(origin_line, pattern)
    if cmp(res_thread_name, 'main') == 0:
        return True
    else:
        return False


def get_tag(origin_data, pattern):
    # origin_data : 2017-07-21 20:28:20:925 I/LBSInfoService:[16282:main] buildWifiInfo getScanResults wifiInfo.ssid =
    # pattern : day time prior/tag:[tid:name] msg
    sub_patterns_array = pattern.split(' ')
    pos = fuzzy_match_array(sub_patterns_array, 'tag')
    if pos < 0:
        return None
    tag_sub_pattern_array, delimiter_array = split_string_character(sub_patterns_array[pos])
    origin_data_array = origin_data.split(' ', pos + 1)
    if len(origin_data_array) <= pos:
        return None
    origin_tag_data = split_string_character_delimiter(origin_data_array[pos], delimiter_array)
    pos = match_array(tag_sub_pattern_array, 'tag')
    if not pos:
        return None
    if not origin_tag_data or len(origin_tag_data) <= pos:
        return None
    return origin_tag_data[pos]


def get_tid(origin_data, pattern):
    # origin_data : 2017-07-21 20:28:20:925 I/LBSInfoService:[16282:main] buildWifiInfo getScanResults wifiInfo.ssid =
    # pattern : day time prior/tag:[tid:name] msg
    sub_patterns_array = pattern.split(' ')
    pos = fuzzy_match_array(sub_patterns_array, 'tid')
    if pos < 0:
        return None
    tid_sub_pattern_array, delimiter_array = split_string_character(sub_patterns_array[pos])
    origin_data_array = origin_data.split(' ', pos + 1)
    if len(origin_data_array) <= pos:
        return None
    origin_tid_data = split_string_character_delimiter(origin_data_array[pos], delimiter_array)
    pos = match_array(tid_sub_pattern_array, 'tid')
    if not pos:
        return None
    if not origin_tid_data or len(origin_tid_data) <= pos:
        return None
    return origin_tid_data[pos]


def get_thread_name(origin_data, pattern):
    # origin_data : 2017-07-21 20:28:20:925 I/LBSInfoService:[16282:main] buildWifiInfo getScanResults wifiInfo.ssid =
    # pattern : day time prior/tag:[tid:name] msg
    sub_patterns_array = pattern.split(' ')
    pos = fuzzy_match_array(sub_patterns_array, 'name')
    if pos < 0:
        return None
    tid_sub_pattern_array, delimiter_array = split_string_character(sub_patterns_array[pos])
    origin_data_array = origin_data.split(' ', pos + 1)
    if len(origin_data_array) <= pos:
        return None
    origin_name_data = split_string_character_delimiter(origin_data_array[pos], delimiter_array)
    pos = match_array(tid_sub_pattern_array, 'name')
    if not pos:
        return None
    if not origin_name_data or len(origin_name_data) <= pos:
        return None
    return origin_name_data[pos]


def get_log_time(origin_data, pattern):
    # origin_data : 2017-07-21 20:28:20:925 I/LBSInfoService:[16282:main] buildWifiInfo getScanResults wifiInfo.ssid =
    # pattern : day time prior/tag:[tid:name] msg
    sub_patterns_array = pattern.split(' ')
    pos = fuzzy_match_array(sub_patterns_array, 'time')
    if pos < 0:
        return None
    origin_name_data = origin_data.split(' ')
    if not origin_name_data or len(origin_name_data) <= pos:
        return None
    return origin_name_data[pos]


def fuzzy_match_array(data_arr, item):
    # 数组模糊匹配
    if not data_arr:
        return -1
    result = -1
    for index, data_item in enumerate(data_arr):
        pos = data_item.find(item, 0)
        if pos >= 0:
            result = index
            break
    return result


def match_array(data_arr, item):
    # 数组模糊匹配
    if not data_arr:
        return -1
    result = -1
    for index, data_item in enumerate(data_arr):
        cmp_res = cmp(data_item, item)
        if cmp_res == 0:
            result = index
            break
    return result
