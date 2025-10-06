import time 
import csv

csv_path = "excel/liste_action_section_1.csv"

def extract_data_from_CSV(csv):
        
    with open(csv_path, newline='') as action_csv:
        return action_csv.read().splitlines()
    
data = extract_data_from_CSV(csv_path)

actions = []
for i in data[1:]:
    action_data = i.split(',')
    action = { 
        "name": [action_data[0]],
        "price": (int(action_data[1])),
        "benefits": (int(action_data[2].strip().replace('%', '')))
    }
    
    actions.append(action)


    
    

    
