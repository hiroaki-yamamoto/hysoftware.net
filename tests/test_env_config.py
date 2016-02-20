#!/usr/bin/env python
# coding=utf-8

import os

from unittest import TestCase

class EnvironmentTestBase(TestCase):
    '''
    Test Environment configurations
    (Note that this is just an base)
    '''

    def setUp(self):
        if type(self) is EnvironmentTestBase:
            raise TypeError("This class is abstract class")
        self.env_backup = os.environ.get("mode", None)

    def tearDown(self):
        if self.env_backup:
            os.environ["mode"] = self.env_backup
        else:
            os.environ.pop("mode", None)
        print(os.environ.get("mode", None))

class DevelopmentTestClass(EnvironmentTestBase):
    '''
    Test Development Mode
    '''

    def setUp(self):
        super().setUp()
        os.environ["mode"] = "devel"

    def test_development_mode(self):
        '''
        Devel Config should be read
        '''
        from app.config import DevelConfig
        self.assertIsNotNone(DevelConfig)

    def test_production_mode(self):
        '''
        Production config should raise an error
        '''
        with self.assertRaises(ImportError):
            from app.config import Production
