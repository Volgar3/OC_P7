import time 
import csv

csv_path = "excel/liste_action_section_1.csv"

def extract_data_from_CSV(csv):
        
    with open(csv_path, newline='') as action_csv:
        return action_csv.read().splitlines()


def clean_data():
    
    brut_actions = extract_data_from_CSV(csv_path)
        
    actions = []
    for i in brut_actions[1:]:
        action_data = i.split(',')
        action = [action_data[0]]
        action.append(action_data[1])
        action.append(int(action_data[2].strip().replace('%', '')))
        actions.append(action)
            
    return actions 

sorted_actions = clean_data()

# --- Print all actions ---
# for action in sorted_actions:
#     print(action)
# print(type(sorted_actions[0][2]))

