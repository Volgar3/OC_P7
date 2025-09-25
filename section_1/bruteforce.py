import time 
import csv

data_path = "excel/liste_action_section_1.csv"

def extract_data_from_CSV(csv):

    data_path = csv
    with open(data_path, newline='') as action_csv:
        
        data = []
        for line in action_csv:
            data.append(line)
    
    return data


def clean_data():
    
    brut_actions = extract_data_from_CSV(data_path)
        
    actions = []
    for i in brut_actions[1:]:
        action_data = i.split(',')
        action = [action_data[0]]
        action.append(action_data[1])
        action.append(int(action_data[2].strip().replace('%', '')))
        actions.append(action)
            
    return actions 



sorted_actions = clean_data()
for action in sorted_actions:
    print(action)
print(type(sorted_actions[0][2]))