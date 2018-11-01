class Node:
    def __init__(self, firstdata):
        self.data = firstdata
        self.nextdata = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.nextdata

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.nextdata = newnext


class CollectionList:
    def __init__(self):
        self.head = None
        self.first = None
        pass

    def __iter__(self):
        return self

    def next(self):  # Python 3: def __next__(self)
        if self.head.getNext() is None:
            raise StopIteration
        else:
            return self.head

    def __len__(self):
        actual = self.first
        count = 0
        while actual is not None:
            count += 1
            actual = actual.getNext()
        return count

    def is_empty(self):
        return self.head is None

    def append(self, data):
        temp = Node(data)
        temp.setNext(self.head)
        if self.is_empty():
            self.first = self.head
        self.head = temp

    def __getitem__(self, key):
        if key < 0 or self.is_empty():
            pass
        else:
            index = 0
            actual = self.first
            found = False
            while not found:
                if index == key:
                    found = True
                elif actual.getNext() is not None:
                    actual = actual.getNext()
                index += 1
            if found:
                return actual.getData()

    def __setitem__(self, key, value):
        if key < 0:
            pass
        else:
            index = 0
            for item in self:
                if index == key:
                    item.setData(value)
                    return None
                index += 1
