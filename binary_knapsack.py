# Items: (weight, value)
items = [(0, 0), (1, 1), (2, 5), (3, 6), (4, 7),
         (5, 8), (6, 10), (7, 11), (8, 12)]
capacity = 12

# Initialize the DP table
dp = [[0 for _ in range(capacity + 1)] for _ in range(len(items))]

# Fill the DP table
for i in range(1, len(items)):
    for w in range(capacity + 1):
        if items[i][0] <= w:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1]
                           [w - items[i][0]] + items[i][1])
        else:
            dp[i][w] = dp[i - 1][w]

# Print the DP table
print("   ", end="")
for w in range(capacity + 1):
    print(f"{w:4}", end="")
print()

for i, row in enumerate(dp):
    print(f"{i:2}", end=" ")
    for value in row:
        print(f"{value:4}", end="")
    print()

# Backtrack to find the selected items
selected_items = []
i, w = len(items) - 1, capacity
while i > 0 and w > 0:
    if dp[i][w] != dp[i - 1][w]:
        selected_items.append(i)
        w -= items[i][0]
    i -= 1

print("\nSelected items:", selected_items[::-1])
print("Total value:", dp[-1][-1])
