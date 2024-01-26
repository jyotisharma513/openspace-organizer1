import pandas as pd
import random

def load_colleagues(colleagues):
    
    df = pd.read_csv("colleagues.txt", sep="\t")
    names = df["name"].tolist()

def load_conditions(colleagues):
    
    return pd.read_csv(colleagues.txt)[["Name1", "Name2", "Condition"]].to_dict("records")

def check_condition(name1, name2, condition):
    
    if condition == "next":
        return abs(name1 - name2) == 1
    elif condition == "not next":
        return abs(name1 - name2) 
    else:
        return False 