from itertools import combinations


def extract_data_from_CSV(csv):
    ''' Extraction from csv ''' 
    with open(csv_path, newline='') as action_csv:
        return action_csv.read().splitlines()
    
def data_treatement():
    ''' Actions formated in dict and put on a list'''
    
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
    ''' Obtenir le nombre de combinaisons possible selon un nombre d'action 
    prit en compte avec une limite de prix d'achat d'action '''
    result_comb_total = []
    for i in range(1, len(actions)):
        result_comb = combinations(actions, i + 1)
        result_comb_total.append([item for item in result_comb])
    
    # for line_comb in result_comb_total:
    #     print(len(line_comb))
    # Print les possibiltés de combinaisons possible sans limite de prix 

    for i in range(len(result_comb_total)):
        combinations_filtered = []
        for comb in result_comb_total[i]:
            total_budget = sum([action['price'] for action in comb])
            if total_budget <= 500:
                combinations_filtered.append(comb)
        result_comb_total[i] = combinations_filtered
        
    return result_comb_total

def best_combination_for_number_of_actions():
    ''' Obtenir la meilleure combinaison pour un nombre d'actions données '''
    result_comb_total = get_combinations(actions, budget)
    best_comb_per_number_of_actions = []
    for i in range (len(result_comb_total)):
        comb_of_action = result_comb_total[i]
        if comb_of_action: # In case if comb = 0
            best_comb = max(comb_of_action, key=lambda comb: sum(action['euros_benefits']for action in comb)
            )
            best_comb_per_number_of_actions.append(best_comb)
        
    for best_comb in best_comb_per_number_of_actions:
        noms = ", ".join(action['name'] for action in best_comb)  # noms des actions
        prix_total = sum(action['price'] for action in best_comb)
        benef_total = sum(action['euros_benefits'] for action in best_comb)
        print(f"{len(best_comb)} actions : {noms} - Prix total: {prix_total} € - Bénéfice total: {benef_total:} €")
    
    return best_comb_per_number_of_actions

def best_comb():
    ''' Give the best combination '''
    best_combs = best_combination_for_number_of_actions()
    the_greatesque = max(best_combs, key=lambda comb: sum(action['euros_benefits'] for action in comb))
    print('--------')
    print(f"La meilleure combinaison est {the_greatesque}")
    print('--------')

# --- Initialisation ---
csv_path = "excel/liste_action_section_1.csv"
actions = data_treatement()
actions.sort(key=lambda item: item['euros_benefits'], reverse=True)
budget = 500
get_combinations(actions, budget)
best_comb()

