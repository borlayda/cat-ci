"""
 A flow is a specific order of steps.
"""

from Item import Item

class Flow(Item):

    def __init__(self, name, steps, description = ""):
        super(Flow, self).__init__(name, description)
        self.steps = steps
        self.db.save(self)
        self.save()
