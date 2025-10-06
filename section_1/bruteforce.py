import time 
import csv

csv_path = "excel/liste_action_section_1.csv"

def extract_data_from_CSV(csv):
        
    with open(csv_path, newline='') as action_csv:
        return action_csv.read().splitlines()
    

def data_treatement():
    
    data = extract_data_from_CSV(csv_path)
    actions = []
    for i in data[1:]:
        action_data = i.split(',')
        action = { 
            "name": action_data[0],
            "price": (int(action_data[1])),
            "benefits_after_2_years": ((int(action_data[1]) * int(action_data[2].strip().replace('%', '')) / 100)) + int(action_data[1])
        }
        actions.append(action)
    return actions

actions = data_treatement()

for action in actions:
    print(action)
    
    
    
    

    
