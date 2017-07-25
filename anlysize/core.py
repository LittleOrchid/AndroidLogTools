# -*- coding: utf-8 -*-
from anlysize.methods import helpers, string_utils


def scan_log_analysis(log_path, activity="com.alipay.mobile.scan.as.main.MainCaptureActivity",
                      pattern="day time prior/tag:[tid:name] msg"):
    results = []
    max_round = 1
    with open(log_path) as log_file:
        result = []
        exec_round = 0
        result_start_analysis = False
        last_line = None
        for line in log_file:
            if exec_round >= max_round:
                continue
            if not helpers.check_log_line_from_main(line, pattern):
                continue
            result_code = scan_analysis_main_thread(activity, pattern, line)
            if result_code == "NONE":
                continue
            elif result_code == "BLOCK_BEGIN":
                result_start_analysis = True
                print line
            elif result_code == "BLOCK_END":
                if not result_start_analysis:
                    continue
                else:
                    result_start_analysis = False
                    exec_round += 1
                    print line
            else:
                if result_start_analysis:
                    time = helpers.get_log_time(line, pattern)
                    string_utils.str_time_long(time)
                    print line


def scan_analysis_main_thread(activity, pattern, origin_data):
    activity_start_features = ["com.alipay.mobile.framework.exception.StartActivityRecord", activity]
    activity_end_log = activity + "|finish"
    if not origin_data:
        return "NONE"
    elif string_utils.string_contains_features(origin_data, activity_start_features):
        return "BLOCK_BEGIN"
    elif origin_data.find(activity_end_log) >= 0:
        return "BLOCK_END"
    else:
        return "NORM"


scan_log_analysis("/Users/RexNJC/Downloads/2661867/2017072120_com.eg.android.AlipayGphone-main.2nd_decode.txt")
