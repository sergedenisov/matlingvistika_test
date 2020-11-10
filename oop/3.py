class train_ticket:
    num_ticket = 0
    def __init__(self, train_num):
        self.train_num = train_num
        self.passenger = []

    def add_passenger(self, passenger_name):
        self.num_ticket += 1
        self.passenger.append([passenger_name,self.num_ticket])



train1 = train_ticket('Pervoe')


train1.add_passenger('Paul')
train1.add_passenger('Irina')
train1.add_passenger('Alex')
train1.add_passenger('Andrew')
train1.add_passenger('Misha')
train1.add_passenger('Vladimir')


print(train1.num_ticket)
print(train1.passenger)
