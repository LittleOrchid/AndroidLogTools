# -*- coding:utf-8 -*-


def format_list_out(result_list, step_num=0):
    if not result_list or len(result_list) == 0:
        return
    step_str = ''
    for index in range(0, step_num):
        step_str += '\t'
    for item in result_list:
        print step_str+item


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

