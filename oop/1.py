class box:
    num_objects = 0
    def __init__(self, nick):
        self.nick = nick

        self.contents = []

    def add_object(self, object_name):
        self.contents.append(object_name)
        box.num_objects += 1

    def remove_object(self, object_name):
        self.contents.remove(object_name)
        box.num_objects -= 1


box1 = box('First Box')

box1.add_object('shoe')
box1.add_object('hat')
box1.add_object('pants')
box1.add_object('hat')

box1.remove_object('hat')

print(box1.num_objects)
print(box1.contents)
