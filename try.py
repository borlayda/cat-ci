#!/usr/bin/env python
"""
 This module is created for trying codes,
 under construction.
"""
from model.pipe import Pipe
from model.task import Task
from utils.execution.command import Command

def main():
    """ Main function """
    task1 = Task("List")
    task2 = Task("Print")
    task3 = Task("Process")

    task1.add_command_obj(Command("ls"))
    task2.add_command_obj(Command("echo", ["My name is Daniel"]))
    task3.add_command_obj(Command("ps"))
    task3.add_command_obj(Command("echo done"))

    pipe = Pipe()
    pipe.add_task(task1)
    pipe.add_task(task2)
    pipe.add_task(task3)

    pipe.execute_pipe()

if __name__ == "__main__":
    main()
