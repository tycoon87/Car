class Car(object):
    def __init__(self,price,speed,fuel,milage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.milage = milage
        self.tax = 0.12
        if self.price > 10000:
            self.tax = 0.15
        
    def display_all(self):
        temp = self.price * self.tax
        self.price = self.price + temp
        print "price: ${}" .format(self.price), "speed: {}".format(self.speed), "fuel: {}".format(self.fuel), "Milage: {}".format(self.milage), "Tax: {}".format(self.tax)
        return self
    
car1 = Car(2000, "35mph", "Full" , 15)
car1.display_all()

