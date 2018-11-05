from src.Angelica.kata1_11.ObjectType import ObjectType


class CollectionList(object):

    def __init__(self):
        self.data = None

    def append(self, t_object):
        index = 0
        if self.data is None:
            self.data = ObjectType(index, t_object)
        elif self.data.temp_data is None:
            index = self.data.data[0]
            self.data.temp_data = ObjectType(index + 1, t_object)
