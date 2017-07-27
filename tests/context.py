# -*- coding: utf-8 -*-
from analyze.tools import main_log_tool
from analyze.tools import computeloginterval
from analyze.methods import format_out
from analyze.methods import pair_stack


def scan_log_analysis():
    print "1. ======================= Test scan_log_analysis==================================="
    file_path = "/Users/RexNJC/Downloads/2661867/2017072120_com.eg.android.AlipayGphone-main.2nd_decode.txt"
    scan_log_tool = main_log_tool.ScanLogTool(log_path=file_path)
    tag_list = scan_log_tool.scan_log_analysis()
    format_out.format_out(tag_list)


def compute_log_interval():
    # 07-27 11:52:27.661  6032  6032 I TaskPoolExecutor: [main] resume execute:URGENT
    print "2. ======================= Test compute_log_interval==================================="
    file_path = "/Users/RexNJC/Downloads/2661867/test.txt"
    log_computed_repo = [
        pair_stack.LogOnOffPair("1", ["TaskPoolExecutor: [main] resume execute:URGENT"],
                                ["TaskPoolExecutor: [main] end resume execute:URGENT"]),
        pair_stack.LogOnOffPair("2", ["TaskPoolExecutor: [main] resume execute:ORDERED"],
                                ["TaskPoolExecutor: [main] end resume execute:ORDERED"]),
        pair_stack.LogOnOffPair("3", ["TaskPoolExecutor: [main] resume execute:NORMAL"],
                                ["TaskPoolExecutor: [main] end resume execute:NORMAL"])
    ]
    log_interval_tool = computeloginterval.ComputeLogInterval(file_path, log_computed_repo,
                                                              "day time pid tid prior tag name msg")
    result_map = log_interval_tool.compute_log_interval()
    format_out.format_out(result_map)


