class Node:
    def __init__(self, firstdata):
        self.data = firstdata
        self.nextnode = None

    def getdata(self):
        return self.data

    def getnext(self):
        return self.nextnode

    def setdata(self, newdata):
        self.data = newdata

    def setnext(self, newnext):
        self.nextnode = newnext

    def __str__(self):
        return str(self.data)


class CollectionList:
    def __init__(self):
        self.head = None
        self.first = None
        self.current = self.first

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
            return None
        else:
            index = 0
            for item in self:
                if index == key:
                    return item
                index += 1

    def __setitem__(self, key, value):
        if key < 0 or self.is_empty():
            return None
        else:
            index = 0
            actual = self.first
            while index <= key:
                if index == key:
                    actual.setdata(value)
                elif actual.getnext() is not None:
                    actual = actual.getnext()
                index += 1

    def __repr__(self):
        separator = ", "
        collection_as_str = CollectionList()
        for item in self:
            collection_as_str.append(str(item))
        return "[" + separator.join(collection_as_str) + "]"

    def insert(self, key, value):
        temp = Node(value)
        index = 0
        actual = self.first
        last = None
        while index <= key:
            if key >= len(self):
                self.append(value)
                return
            if index >= key:
                if index < 1:
                    temp.setnext(actual)
                    self.first = temp
                else:
                    temp.setnext(actual)
                    last.setnext(temp)
                return
            elif actual.getnext() is not None:
                last = actual
                actual = actual.getnext()
            index += 1

    def remove(self, value):
        index = 0
        actual = self.first
        last = None
        while actual is not None:
            if actual.getdata() == value:
                last.setnext(actual.getnext())
                if index == 0:
                    self.first = last
                break
            else:
                last = actual
                actual = actual.getnext()
            index += 1
