items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    item_ratio = [(name, data["cost"], data["calories"], data["calories"] / data["cost"]) for name, data in items.items()]
    item_ratio.sort(key=lambda x: x[3], reverse=True)

    total_calories = 0
    total_cost = 0
    chosen_items = []

    for name, cost, calories, ratio in item_ratio:
        if total_cost + cost <= budget:
            chosen_items.append(name)
            total_cost += cost
            total_calories += calories

    return chosen_items, total_calories, total_cost

budget = 100
chosen_items, total_calories, total_cost = greedy_algorithm(items, budget)
print(f"Вибрані страви: {chosen_items}")
print(f"Сумарна калорійність: {total_calories}")
print(f"Загальна вартість: {total_cost}")

def dynamic_programming(items, budget):
    item_names = list(items.keys())
    item_costs = [items[item]["cost"] for item in item_names]
    item_calories = [items[item]["calories"] for item in item_names]
    n = len(item_names)
    
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(budget + 1):
            dp[i][j] = dp[i - 1][j]
            if item_costs[i - 1] <= j:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - item_costs[i - 1]] + item_calories[i - 1])
    
    total_calories = dp[n][budget]
    chosen_items = []
    j = budget
    
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            chosen_items.append(item_names[i - 1])
            j -= item_costs[i - 1]
    
    chosen_items.reverse()
    total_cost = sum(items[item]["cost"] for item in chosen_items)
    
    return chosen_items, total_calories, total_cost

chosen_items, total_calories, total_cost = dynamic_programming(items, budget)
print(f"Вибрані страви: {chosen_items}")
print(f"Сумарна калорійність: {total_calories}")
print(f"Загальна вартість: {total_cost}")