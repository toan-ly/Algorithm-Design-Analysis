class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight if weight > 0 else 0

def fractional_knapsack(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    sorted_items = sorted(items, key=lambda x: x.ratio, reverse=True)

    total_value = 0
    knapsack = []

    for item in sorted_items:
        if capacity >= item.weight:
            knapsack.append((item, 1))
            total_value += item.value
            capacity -= item.weight
        else:
            fraction = capacity / item.weight
            knapsack.append((item, fraction))
            total_value += item.value * fraction
            break

    return total_value, knapsack

def zero_one_knapsack(items, capacity):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if items[i - 1].weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1]
                               [w - items[i - 1].weight] + items[i - 1].value)
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find selected items
    w = capacity
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append((items[i - 1], 1))
            w -= items[i - 1].weight

    return dp[n][capacity], selected_items[::-1]


# Define items
items = [
    Item(1, 1),   # Item 1
    Item(2, 5),   # Item 2
    Item(3, 6),   # Item 3
    Item(4, 7),   # Item 4
    Item(5, 8),   # Item 5
    Item(6, 10),  # Item 6
    Item(7, 11),  # Item 7
    Item(8, 12)   # Item 8
]

capacity = 12

# Solve Fractional Knapsack
frac_value, frac_knapsack = fractional_knapsack(items, capacity)

print("Fractional Knapsack Solution:")
print(f"Total Value: {frac_value}")
print("Selected Items:")
for item, fraction in frac_knapsack:
    print(
        f"Item (weight: {item.weight}, value: {item.value}) - Fraction: {fraction:.2f}")

print("\n" + "=" * 50 + "\n")

# Solve 0-1 Knapsack
zero_one_value, zero_one_knapsack = zero_one_knapsack(items, capacity)

print("0-1 Knapsack Solution:")
print(f"Total Value: {zero_one_value}")
print("Selected Items:")
for item, _ in zero_one_knapsack:
    print(f"Item (weight: {item.weight}, value: {item.value})")

# Calculate total weight for 0-1 knapsack
total_weight = sum(item.weight for item, _ in zero_one_knapsack)
print(f"\nTotal Weight: {total_weight}")
