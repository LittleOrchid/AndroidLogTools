# -*- coding: utf-8 -*-


class Config:

    def __init__(self, activity):
        self.activity = activity
        # 扫码生命周期对应的日志
        self.scan_lifecycle_tag = {
            'in': ["com.alipay.mobile.framework.exception.StartActivityRecord", activity],
            'onCreate': '',
            "onResume": '',
            "onPause": '',
            "onDestroy": '',
            "out": [activity + "|finish"]
        }


