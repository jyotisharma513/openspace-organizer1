from src.table import Table
from src.utils import load_colleagues
import random
import pandas as pd

class OpenSpace:
 def __init__(self, tables, number_of_tables):
         self.tables =  [(Table(i+1)) for i in range(6) ]
         self.number_of_tables=6
         
 def organize(self, names):
        
        seats = []
        for table in self.tables:
            seats.extend(table.seats) # add the seats of each table to the list
        random.shuffle(names) 
        for j in range(len(names)):
         if j < len(seats):
          seats[j].occupant = names[j]
       
 def display(self):     
    for i, table in enumerate(self.tables):
            print(f"Table {i+1}:")
            table.display()
            print()

def store(self):
         data = []
         for i, table in enumerate(self.tables):
            for j, seat in enumerate(table.seats):
                data.append({"Table": i+1, "Seat": j+1, "Name": seat.occupant})
         df = pd.DataFrame(data) 
         df.to_csv('colleagues.txt', sep='\t', index=False)


openspace=OpenSpace([(Table(i+1)) for i in range(6) ],6)
