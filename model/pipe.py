#!/usr/bin/env python
"""
 Pipe module
 -----------

 This module is responsible for use-cases of
 the pipelines. It contains an object to represent
 the pipeline itself, and some functions to operate
 with those objects.
"""

import logging
import sys

LOGGER = logging.getLogger("Pipeline")
LOGGER.setLevel(logging.INFO)
SH = logging.StreamHandler(sys.stdout)
SH.setLevel(logging.INFO)
FORMATTER = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
SH.setFormatter(FORMATTER)
LOGGER.addHandler(SH)

class Pipe(object):
    """
    Pipe object for soring data about the
    retalted tasks, which defines a whole
    pipeline. Also it has the information
    about the input and output.
    """

    def __init__(self):
        """ Constructor of the class """
        self.tasks = []
        self.result = None
        self.commands = []

    def add_task(self, new_task):
        """ Adds a new task at the end of the pipeline """
        self.tasks.append(new_task)

    def execute_pipe(self):
        """ Executes the tasks in the pipline in order """
        for task in self.tasks:
            LOGGER.info("%s started: ", task.name)
            task.execute_task()
