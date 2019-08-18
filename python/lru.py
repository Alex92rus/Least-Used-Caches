

class Entry:

    def __init__(self, key, value):
        self.left = None
        self.right = None
        self.key = key
        self.value = value


class Lru:

    def __init__(self):
        self.start = None
        self.end = None
        self.entryMap = {}
        self.lruSize = 4

    def getEntry(self, key):
        if key in self.entryMap:
            entry = self.entryMap[key]
            self._removeEntry(entry)
            self._addAtStart(entry)
            return entry
        else:
            return -1

    def addEntry(self, key, value):
        if key in self.entryMap:
            entry = self.entryMap[key]
            entry.value = value
            self._removeEntry(entry)
            self._addAtStart(entry)
        else:
            newEntry = Entry(key, value)
            if len(self.entryMap) == self.lruSize:
                self._removeEntry(self.end)
            self.entryMap[key] = newEntry
            self._addAtStart(newEntry)

    def _removeEntry(self, entry):

        if entry.right is not None:
            entry.right.left = entry.left
        else:
            self.end = entry.left

        if entry.left is not None:
            entry.left.right = entry.right
        else:
            self.start = entry.right

    def _addAtStart(self, entry):

        if self.start is not None:
            self.start.left = entry

        entry.right = self.start
        self.start = entry

        if self.end is None:
            self.end = self.start

    def printDoublyLinkedList(self):
        iterDL = self.start
        while iterDL is not None:
            print("({}->{})=>".format(iterDL.key, iterDL.value), end="")
            iterDL = iterDL.right
        print("None")

    def getCacheInOrder(self, lastFirst=True):
        res = []
        iterDL = self.start if lastFirst else self.end
        while iterDL is not None:
            res.append(iterDL.value)
            iterDL = iterDL.right if lastFirst else iterDL.left
        return res


if __name__ == '__main__':
    lru = Lru()
    lru.addEntry(4, 16)
    lru.addEntry(3, 9)
    lru.printDoublyLinkedList()
