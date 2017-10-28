"""
 The pipeline is a specific set of flows orderly executed.
 This object can describe this functionality.
"""

from Item import Item

class Pipeline(Item):

    def __init__(self, name, flows, description = ""):
        super(Pipeline, self).__init__(name, description)
        self.flows = flows
        self.db.save(self)
        self.save()
