from src.openspace import OpenSpace
from src.table import Table 
import random
import pandas as pd
if __name__ == "__main__":

 with open('colleagues.txt', 'r') as f:
    names = [line.strip() for line in f.readlines()]
    print(names)


tables = [(Table(i+1)) for i in range(6) ]
openspace = OpenSpace(tables, 6)
openspace.organize(names) 
openspace.display() 
openspace.store("repartition.txt") 

    

   