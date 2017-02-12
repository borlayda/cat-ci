#!/usr/bin/env python
"""
 This is the module to run codes.
"""

import subprocess


class Command(object):
    """
    This object represents a command, which
    has to be executed.
    """

    def __init__(self, command, args=()):
        self.command = command
        self.args = args
        self.output = ""
        self.error = ""
        self.returncode = None

    def execute(self):
        """ Runs the command with it's parameters. """
        if self.args:
            self.command = self.command + ' ' + ' '.join(self.args)
        popen = subprocess.Popen(self.command,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 shell=True)
        self.output, self.error = popen.communicate()
        self.returncode = popen.returncode

    def is_done(self):
        """ Tells if the command has been executed. """
        return self.returncode is not None
