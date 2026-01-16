import time

def extract_data_from_CSV(csv_path):
    with open(csv_path, newline="") as action_csv:
        return action_csv.read().splitlines()

def data_treatement():
    data = extract_data_from_CSV(csv_path)
    actions = []
    for line in data[1:]:
        action_data = line.split(",")
        action = {
            "name": action_data[0],
            "price": int(action_data[1]),
            "percentage_benefits": int(action_data[2].strip().replace("%", "")),
            "euros_benefits": int(action_data[1]) * int(action_data[2].strip().replace("%", "")) / 100,
        }
        actions.append(action)
    return actions

def sac_a_dos(actions, budget):
    matrice = [0] * (budget + 1)
    selected_actions = [ [] for _ in range(budget + 1) ]
    for action in actions:
        price = action["price"]
        benefits = action["euros_benefits"]
        for combinations in range(budget, price - 1, -1):
            if matrice[combinations - price] + benefits > matrice[combinations]:
                matrice[combinations] = matrice[combinations - price] + benefits
                selected_actions[combinations] = selected_actions[combinations - price] + [action]
    best_combination = max(range(budget + 1), key=lambda x: matrice[x])
    return selected_actions[best_combination]

def best_comb():
    start_time = time.time()
    best_combination = sac_a_dos(actions, budget)
    end_time = time.time()
    
    names = ", ".join(action["name"] for action in best_combination) 
    number_of_actions = len(best_combination)
    total_cost = sum(action["price"] for action in best_combination)
    total_benefits = sum(action["euros_benefits"] for action in best_combination)
    
    print("--------")
    print(f"Temps d'exécution : {end_time - start_time} secondes")
    print(f"La meilleure combinaison se compose de {number_of_actions} actions, coûte = {total_cost} € et génère un bénéfice de {total_benefits} après 2 ans. Actions: {names}")
    print("--------")
    return best_combination

# --- Initialisation ---

csv_path = "excel/liste_action_section_1.csv"
actions = data_treatement()
actions.sort(key=lambda item: item["euros_benefits"], reverse=True)
budget = 500

best_comb()