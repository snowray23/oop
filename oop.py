class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
#task1 update owener to new owner 
    def update_owner(self, new_owner):
        self.owner = new_owner
        print("new owner added")

#to demonstrate
car1 = Vehicle("123aba", "Car", "Ray")
car2 = Vehicle("abc123", "truck", "John")
print(f"car1 belongs to {car1.owner}")
print(f"car2 belongs to {car2.owner}")

car1.update_owner("Jack")
car2.update_owner("Kelly")
print(f"car1 now belongs to {car1.owner}")
print(f"car2 now belongs to {car2.owner}")

#task adding a method to track count
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  # current count at 0

    # task adding participant 
    def add_participant(self):
        self.participant_count += 1
        print(f"New participant was added to {self.name}. The current count is {self.participant_count}")

    # task returns the current count
    def get_participant_count(self):
        return self.participant_count

event_one = Event("gaming night", "11,11,2031")
event_one.add_participant()