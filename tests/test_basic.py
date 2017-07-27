# -*- coding: utf-8 -*-

import context

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    @staticmethod
    def test_log_analysis():
        context.scan_log_analysis()

    @staticmethod
    def test_log_interval():
        context.compute_log_interval()


if __name__ == '__main__':
    unittest.main()

