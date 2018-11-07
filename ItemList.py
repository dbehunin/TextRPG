from item import item

class ItemList:

    list = []

    def __init__(self, txt):
        temp = []
        i = 0
        file = open(txt, "r")
        data = file.readlines()
        for line in data:
            items = line.split()
            newItem = item(items)
            self.list.append(newItem)
            i += 1
        file.close()

    def getItem(self, name):
        for i in range(len(self.list)):
            if name == self.list[i].name:
                return self.list[i]
