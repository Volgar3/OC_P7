from itertools import combinations

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
            "percentage_benefits": int(action_data[2].strip().replace('%', '')),
            "euros_benefits": ((int(action_data[1]) * int(action_data[2].strip().replace('%', '')) / 100))
        }
        actions.append(action)
    return actions

def get_combinations(actions, budget):
    result_comb_total = []
    for i in range(1, len(actions)):
        result_comb = combinations(actions, i + 1)
        result_comb_total.append([item for item in result_comb])
    
    for line_comb in result_comb_total:
        print(len(line_comb))

    for i in range(len(result_comb_total)):
        total_budget = 0
        for comb in result_comb_total[i]:
            total_budget = sum([action['euros_benefits'] for action in comb])
        if total_budget > 500:
            result_comb_total[i].pop(comb)

    for line_comb in result_comb_total:
        print(len(line_comb))


actions = data_treatement()
actions.sort(key=lambda item: item['euros_benefits'], reverse=True)
budget = 500
get_combinations(actions, 500)