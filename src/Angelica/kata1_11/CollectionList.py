from src.Angelica.kata1_11.ObjectType import ObjectType


class CollectionList(object):

    @property
    def __index__(self, index):
        return index

    def __init__(self):
        self.data = None

    @staticmethod
    def append(self, t_object):
        index = 0
        if ObjectType.get_temp_object() is None:
            ObjectType(index,t_object)
            index += 1
            self.__index__(index)
        else:
            index += 1
            ObjectType.set_object(index,t_object)
            self.__index__(index)

    def __len__(self):
        return self.__index__

    @staticmethod
    def get_index(index):
        obj = ObjectType.get_object()
        obj_tmp = ObjectType.get_temp_object()

        if obj[0] == index:
            return obj[1]
        elif obj_tmp[0] == index:
            return obj_tmp[1]


