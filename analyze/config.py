# -*- coding: utf-8 -*-


class Config:
    NONE = "none"
    IN = "in"
    ON_CREATE = "onCreate"
    ON_RESUME = "onResume"
    ON_PAUSE = "onPause"
    ON_DESTROY = "onDestroy"
    OUT = "out"
    NORM = "norm"

    def __init__(self, activity):
        self.activity = activity
        # 扫码生命周期对应的日志
        self.scan_lifecycle_tag = {
            'in': ['com.alipay.mobile.framework.exception.StartActivityRecord', activity],
            'onCreate': ['BaseFragment: onCreate()'],
            "onResume": ['BaseScanFragment: onResume()'],
            "onPause": ['BaseScanFragment: onPause()'],
            "out": [activity + "|finish"]
        }


