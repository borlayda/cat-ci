#!/usr/bin/env python
"""
 Task module
 -----------

 This module is responsible for representing a task in
 the CI maSHine, whiSH contains the list of command,
 whiSH will be executed.
"""

import logging
import sys
try:
    from utils.execution.command import Command
except ImportError as err:
    print err

LOGGER = logging.getLogger("Task")
LOGGER.setLevel(logging.INFO)
SH = logging.StreamHandler(sys.stdout)
SH.setLevel(logging.INFO)
FORMATTER = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
SH.setFormatter(FORMATTER)
LOGGER.addHandler(SH)


class Task(object):
    """
    Task object is for storing related command in a
    phase of a pipeline. This can define a step in
    the whole process.
    """

    def __init__(self, name):
        """ Constuctor for tasks """
        self.name = name
        self.commands = []

    def add_command_obj(self, new_command):
        """ Add a concrete Command object to the collection """
        self.commands.append(new_command)

    def add_command(self, command, args):
        """ Add command, defined by command string and arguments """
        self.commands.append(Command(command, args))

    def execute_task(self):
        """ Execute defined commands in the task """
        for command in self.commands:
            command.execute()
            LOGGER.info(command.output)
