class Car(object):
    def __init__(self,model,color,company,speedLimit):
        self.color=color
        self.model=model
        self.company=company
        self.speedLimit=speedLimit
    def start(self):
        print("started")
    def stop(self):
        print("stopped")
    def accelerate(self):
        print("accelerated")
Honda=Car("Model1","blue","Honda","125")
print(Honda.color)

class Sandwhich(object):
    def __init__(self,breadType,ingriediant1,ingriediant2,ingriediant3):
        self.ingriediant1=ingriediant1
        self.breadType=breadType
        self.ingriediant2=ingriediant2
        self.ingriediant3=ingriediant3
    def start(self):
        print("started")
    def stop(self):
        print("stopped")
    def accelerate(self):
        print("accelerated")
sandwhich1=Sandwhich("Whole grain","penut butter","Jam","banana")
test=input("Do you want to know Bread type, 1st ingrediant, 2nd ingrediant, or 3rd ingrediant?")
if(test=="Bread type"):
    print(sandwhich1.breadType)
elif(test=="1st ingrediant"):
    print(sandwhich1.ingriediant1)
elif(test=="2nd ingrediant"):
    print(sandwhich1.ingriediant2)
elif(test=="3rd ingrediant"):
    print(sandwhich1.ingriediant3)