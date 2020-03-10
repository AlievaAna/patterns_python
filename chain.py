class EventGet:
    def __init__(self, type_):
        self.name = "get"
        self.type_ = type_
        

class EventSet:
    def __init__(self, value):
        self.name = "set"
        self.value = value
        
        
class NullHandler:    
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, obj, event):
        if self.__successor is not None:
            return self.__successor.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if event.name == "get":
            if event.type_ == int:
                return obj.integer_field
            else:
                return super().handle(obj, event)
        elif event.name == "set":
            if type(event.value) == int:
                obj.integer_field = event.value
            else:
                super().handle(obj, event)
        else:
            super().handle(obj, event)    


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if event.name == "get":
            if event.type_ == float:
                return obj.float_field
            else:
                return super().handle(obj, event)
        elif event.name == "set":
            if type(event.value) == float:
                obj.float_field = event.value
            else:
                super().handle(obj, event)
        else:
            super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if event.name == "get":
            if event.type_ == str:
                return obj.string_field
            else:
                return super().handle(obj, event)
        elif event.name == "set":
            if type(event.value) == str:
                obj.string_field = event.value
            else:
                super().handle(obj, event)
        else:
            super().handle(obj, event)