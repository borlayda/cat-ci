#!/usr/bin/env python
"""
 Testing module of the command related functions.
"""

import unittest
import sys

sys.path.append('..')
try:
    from utils.execution.command import Command
except ImportError as err:
    print err
    exit(1)


class TestCommand(unittest.TestCase):
    """
    Class to test the command objects functionality.
    """

    def setUp(self):
        self.exec_command = "ls"
        self.test_arguments = ["-l", "*"]
        self.test_wrong_arguments = ["-z", "*"]
        self.exec_str_command = "ls -l *"

    def test_run_command(self):
        """ Tests ls command without parameters """
        test_command = Command(self.exec_command)
        test_command.execute()
        self.assertTrue(test_command.is_done())

    def test_run_str_command(self):
        """ Tests ls command as string """
        test_command = Command(self.exec_str_command)
        test_command.execute()
        self.assertTrue(test_command.is_done())

    def test_command_argumented(self):
        """ Tests ls command with parameters """
        test_command = Command(self.exec_command, self.test_arguments)
        test_command.execute()
        self.assertTrue(test_command.is_done())

    def test_good_arguments(self):
        """ Tests if the ls command fails with good arguments. """
        test_command = Command(self.exec_command, self.test_arguments)
        test_command.execute()
        self.assertEquals(0, test_command.returncode)

    def test_bad_arguments(self):
        """ Tests if the ls command fails with bad arguments. """
        test_command = Command(self.exec_command, self.test_wrong_arguments)
        test_command.execute()
        self.assertEquals(2, test_command.returncode)
