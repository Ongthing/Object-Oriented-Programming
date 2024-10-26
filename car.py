
class Car:

    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def drive(self):
        print("that "+self.model+"is driving")
    def stop(self):
        print("that "+self.model+"is stopped")