# -*- coding:utf-8 -*-


def split_string_character(origin_string):
    if not origin_string or len(origin_string) == 0:
        return None
    result_arr = []
    delimiter_arr = []
    begin = 0
    for index in range(len(origin_string)):
        if origin_string[index].isalnum() or cmp(origin_string[index], '_') == 0:
            continue
        else:
            if index >= begin:
                delimiter_arr.append(origin_string[index])
            if index > begin:
                result_str = origin_string[begin:index]
                result_arr.append(result_str)
            begin = index+1
    return result_arr, delimiter_arr


def split_string_character_delimiter(origin_string, delimiters):
    if not origin_string or len(origin_string) == 0:
        return origin_string
    if not delimiters or len(delimiters) == 0:
        return origin_string
    begin = 0
    delimiter_index = 0
    result_arr = []
    for index in range(len(origin_string)):
        if len(delimiters) <= delimiter_index:
            if index > begin:
                result_str = origin_string[begin:index]
                result_arr.append(result_str)
            break
        if cmp(origin_string[index], delimiters[delimiter_index]) == 0:
            if index > begin:
                result_str = origin_string[begin:index]
                result_arr.append(result_str)
            begin = index + 1
            delimiter_index += 1
    return result_arr


def string_contains_features(origin_data, features):
    if not features:
        return True
    result = True
    for feature in features:
        if origin_data.find(feature) < 0:
            result = False
            break
    return result


def str_time_long(time_str, time_pattern="hh:mm:ss:ms"):
    if cmp(time_pattern, "hh:mm:ss:ms") == 0:
        time_parts = time_str.split(':')
        result = (int(time_parts[0])*3600+int(time_parts[1])*60+int(time_parts[2]))*1000+int(time_parts[3])
        return result
    elif cmp(time_pattern, "hh:mm:ss.ms") == 0:
        time_parts = time_str.split(':')
        result = int(time_parts[0]) * 3600 + int(time_parts[1]) * 60
        ss_parts = time_parts[2].split('.')
        result = (result + int(ss_parts[0])) * 1000 + int(ss_parts[1])
        return result
    else:
        return 0


