#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from kivycrm.kivycrmapp import KivycrmApp


class TestKivycrmApp(unittest.TestCase):
    """TestCase for KivycrmApp.
    """
    def setUp(self):
        self.app = KivycrmApp()

    def test_name(self):
        self.assertEqual(self.app.name, 'kivycrm')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
