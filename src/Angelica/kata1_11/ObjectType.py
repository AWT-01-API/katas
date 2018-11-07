class ObjectType:
    def __init__(self,index, object_type):
        self.data = (index,object_type)
        self.temp_data = None

    def set_object(self,index, other_object):
        self.temp_data = self.data
        self.data = (index, other_object)

    def get_object(self):
        return self.data

    def get_temp_object(self):
        return self.temp_data

