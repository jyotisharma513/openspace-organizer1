class Seat():
    def __init__(self,free,occupant):
        self.free=free
        self.occupant=occupant
    def set_occupant(self,name):
        if self.free==True:
          self.occupant=name
          print(f"{name} has taken the seat.")
        else:
            print(f"The seat is already occupied by {self.occupant}.")
    def remove_occupant(self,NAME):
        if self.free==False and self.occupant ==NAME:
            self.occupant=None
            self.free=True
            print(f"{NAME} has left the seat.")
            return NAME
        else:
            print(f"the seat is not occupied by {NAME}.")


class Table:
 def __init__(self,capacity):

    self.capacity=capacity
    self.seats=[Seat('free','occupant') for _ in range(capacity)]
 def has_free_spot(self):
     return any(seat.free for seat in self.seats)
   
 def assign_seat(self,name):
     for seat in self.seats:
            if seat.set_occupant(name):
                return True
            else:
                return False
 def capacity_left(self):
       return sum(seat.free for seat in self.seats)
 

 seat=Seat(True,'jyoti')
 print(seat.free)

table=Table(20)  
         
         
         
       
     