class Classy(object):
    def __init__(self):
        self.items = []           #create a list for adding items 

    def addItem(self, item):
        self.items.append(item)   # add item to items list 

    def getClassiness(self):
        classiness_points = {     #add points to calculate them when getclassiness is called by somthing
            "tophat": 2,
            "bowtie": 4,
            "monocle": 5
        }
        total_classiness = sum(classiness_points.get(item, 0) for item in self.items) # calculate the total points with sum method
        return total_classiness

# Test cases
me = Classy()

# Should be 0
print(me.getClassiness())

me.addItem("tophat")
# Should be 2
print(me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print(me.getClassiness())

me.addItem("bowtie")
# Should be 15
print(me.getClassiness())
