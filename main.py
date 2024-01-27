from src.openspace import OpenSpace
from src.table import Table 
import random
import pandas as pd
if __name__ == "__main__":

 with open('colleagues.txt', 'r') as f:
    names = [line.strip() for line in f.readlines()]
    print(names)


tables = [(f"table({i+1})-seat({j+1})") for i in range(6) for j in range(4)]

# Loop through the list of names and assign them to tables and seats
with open("seating.txt", "w") as f:
    for i, name in enumerate(names):
        # Remove the newline character from the name
        name = name.strip()
        # Get the table and seat for the name
        table_seat = tables[i]
        # Write the name, table, and seat to the file
        f.write(f"{name} is assigned to {table_seat}\n")
openspace = OpenSpace(tables, 6)
openspace.organize(names) 
openspace.display() 
openspace.store("repartition.txt") 

    

   
