class Seat():
    def __init__(self,free,occupant):
        self.free=free
        self.occupant=occupant
    def set_occupant(self,name):
        if self.free==True:
           self.occupant=='name'
           print(f"{name} has taken the seat.")
        else:
            print(f"The seat is already occupied by {self.occupant}.")
    def remove_occupant(self,NAME):
        if self.free==False and self.occupant =='NAME':
            self.occupant=''
            print(f"{NAME} has left the seat.")
            return NAME
        else:
            print("The seat is already empty.")
            