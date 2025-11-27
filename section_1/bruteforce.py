from itertools import combinations


def extract_data_from_CSV(csv_path):
    """Data extraction from CSV."""
    with open(csv_path, newline="") as action_csv:
        return action_csv.read().splitlines()


def data_treatement():
    """Actions formatted in dict and put into a list."""
    data = extract_data_from_CSV(csv_path)
    actions = []
    for line in data[1:]:
        action_data = line.split(",")
        action = {
            "name": action_data[0],
            "price": int(action_data[1]),
            "percentage_benefits": int(
                action_data[2].strip().replace("%", "")
            ),
            "euros_benefits": int(action_data[1])
            * int(action_data[2].strip().replace("%", ""))
            / 100,
        }
        actions.append(action)
    return actions


def get_combinations(actions, budget):
    """Get all possible combinations for each number of actions."""
    result_comb_total = []
    for i in range(1, len(actions)):
        result_comb = combinations(actions, i + 1)
        result_comb_total.append([item for item in result_comb])

    for i in range(len(result_comb_total)):
        combinations_filtered = []
        for comb in result_comb_total[i]:
            total_budget = sum(action["price"] for action in comb)
            if total_budget <= budget:
                combinations_filtered.append(comb)
        result_comb_total[i] = combinations_filtered

    return result_comb_total


def best_combination_by_number_of_actions():
    """Get all best combinations for each number of actions."""
    result_comb_total = get_combinations(actions, budget)
    best_comb_per_number_of_actions = []
    for comb_of_action in result_comb_total:
        if comb_of_action:  # In case comb_of_action is empty
            best_comb = max(
                comb_of_action,
                key=lambda comb: sum(
                    action["euros_benefits"] for action in comb
                ),
            )
            best_comb_per_number_of_actions.append(best_comb)
    return best_comb_per_number_of_actions


def best_comb():
    """Give the best combination generating the most benefits after 2 years."""
    best_combs = best_combination_by_number_of_actions()
    best_combination_total = max(
        best_combs,
        key=lambda comb: sum(action["euros_benefits"] for action in comb),
    )

    names = ", ".join(action["name"] for action in best_combination_total)
    number_of_actions = len(best_combination_total)
    total_cost = sum(action["price"] for action in best_combination_total)
    total_benefits = sum(
        action["euros_benefits"] for action in best_combination_total
    )
    print("--------")
    print(
        f"La meilleure combinaison se compose de {number_of_actions} "
        f"actions, coûte = {total_cost} € et génère un bénéfice de "
        f"{total_benefits} après 2 ans. Actions: {names}"
    )
    print("--------")


# --- Initialisation ---

csv_path = "excel/liste_action_section_1.csv"
actions = data_treatement()
actions.sort(key=lambda item: item["euros_benefits"], reverse=True)
budget = 500
best_comb()
