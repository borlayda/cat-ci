"""
 The step is an atomic item of the pipeline flow, and it is for describing
 the step that you's like to execute as a part of something.

 It could be an executed command, a file changing operation, or anything you
 need.
"""

from Item import Item

class Step(Item):

    def __init__(self, name, step_desc, description = ""):
        super(Step, self).__init__(name, description)
        self.step_desc = step_desc
        self.db.save(self)
        self.save()
