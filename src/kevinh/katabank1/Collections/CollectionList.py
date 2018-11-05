class Node:
    def __init__(self, firstdata):
        self.data = firstdata
        self.nextdata = None

    def getdata(self):
        return self.data

    def getnext(self):
        return self.nextdata

    def setdata(self, newdata):
        self.data = newdata

    def setnext(self, newnext):
        self.nextdata = newnext


class CollectionList:
    def __init__(self):
        self.head = None
        self.first = None
        self.current = self.first
        pass

    def __iter__(self):
        self.current = self.first
        return self

    def next(self):  # Python 3: def __next__(self)
        if self.current is None:
            raise StopIteration
        else:
            actual = self.current.getdata()
            self.current = self.current.getnext()
            return actual

    def __len__(self):
        actual = self.first
        count = 0
        while actual is not None:
            count += 1
            actual = actual.getnext()
        return count

    def is_empty(self):
        return self.head is None

    def append(self, data):
        temp = Node(data)
        if self.is_empty():
            self.first = temp
            self.head = self.first
        self.head.setnext(temp)
        self.head = temp

    def __getitem__(self, key):
        if key < 0 or self.is_empty():
            pass
        else:
            index = 0
            for item in self:
                if index == key:
                    return item
                index += 1

    def __setitem__(self, key, value):
        if key < 0 or self.is_empty():
            pass
        else:
            index = 0
            actual = self.first
            while index <= key:
                if index == key:
                    actual.setdata(value)
                elif actual.getnext() is not None:
                    actual = actual.getnext()
                index += 1
