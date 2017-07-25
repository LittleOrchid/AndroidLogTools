# -*- coding: utf-8 -*-

import context

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_suits(self):
        context.scan_log_analysis()


if __name__ == '__main__':
    unittest.main()

