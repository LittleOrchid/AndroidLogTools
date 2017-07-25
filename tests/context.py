# -*- coding: utf-8 -*-
import analyze


def scan_log_analysis():
    file_path = "/Users/RexNJC/Downloads/2661867/2017072120_com.eg.android.AlipayGphone-main.2nd_decode.txt"
    scan_log_tool = analyze.ScanLogTool(log_path=file_path)
    tag_list = scan_log_tool.scan_log_analysis()
    print tag_list
    assert tag_list is not None
