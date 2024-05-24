
    

class Car:
    def __init__(self, name, model, per_hr, total):
        self.name = name
        self.model = model
        self.per_hr = per_hr
        self.total = total

    def display(self):
        print(self.name, "\n", self.model, "\n", self.per_hr, "\n", self.total)

# class Rental(Car):
#     def __init__(self, name, model, per_hr, total, quantity):
#         Car.__init__(self, name, model, per_hr, total)
        # self.quantity = quantity
        # self.left = self.total - self.quantity

    # def display_rental(self):
    #     Car.display(self)
        # if self.left < self.quantity:
        #     print("Out of stock by", self.quantity - self.left)
        # elif self.quantity < 0:
        #     print("Enter quantity greater than zero")
        # else:
        #     print("Available")
        #     self.total = self.total - self.quantity
        #     print("Updated quantity", self.total)

list_car = []
while True:
    user_inp = int(input("Enter choice\n1) Add\n2) Rent\n3) Break\n"))
    if user_inp == 1:
        car_name = input("Enter car name: ")
        car_model = input("Enter car model: ")
        per_hr_cost = int(input("Enter per hour cost: "))
        total_car = int(input("Enter total car to add: "))
        car1 = Car(car_name, car_model, per_hr_cost, total_car)
        list_car.append(car1)
    elif user_inp == 2:
        print("Following are the available cars:")
        for j in range(0,len(list_car)):
            print(j,")",end="")
            print(" ",list_car[j].display())
        print("")
        print("Choose a car to rent from 0 to", len(list_car) - 1)
        choice = int(input("Please enter value: "))
        if 0 <= choice < len(list_car):
            print("Chosen car:")
            list_car[choice].display()
        quant=int(input("enter quantity of car to rent"))
        if(quant<list_car[choice].total and quant>0):
            car_left=list_car[choice].total-quant
            rent_price=list_car[choice].per_hr*quant
            print(rent_price)
            print("car left is",car_left)
        elif(quant>list_car[choice].total):
            print("out of stock")
            print("")
    elif user_inp == 3:
        print("Thank you For Visiting !!")
        break
