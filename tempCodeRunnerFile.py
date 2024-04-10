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
print(f"car1 belongs to car1{car1.owner}")
print(f"car1 belongs to car1{car2.owner}")

car1.update_owner("Jack")
car2.update_owner("Kelly")
print(f"car1 now belongs to {car1.owner}")
print(f"car2 now belongs to {car2.owner}")
    