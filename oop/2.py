class box:
    num_objects = 0
    contents = []

    def add_object(self, object_name):
        self.contents.append(object_name)
        box.num_objects += 1


class box_remove:
    def __init__(self):
        self.removelist = []

    def add_to_remove_list(self, object_name):
        self.removelist.append(object_name)

    def execute_removal(self, target):
        for x in self.removelist:
            target.contents.remove(x)
            target.num_objects -= 1



box1 = box()
remove1 = box_remove()


box1.add_object('shoe')
box1.add_object('hat')
box1.add_object('pants')
box1.add_object('hat')

remove1.add_to_remove_list('hat')
remove1.add_to_remove_list('shoe')


remove1.execute_removal(box1)

print(box1.num_objects)
print(box1.contents)
