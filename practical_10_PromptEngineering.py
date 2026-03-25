import math

def minimax(stones, is_max, depth, max_depth):
    if stones == 0:
        return -1 if is_max else 1
    if depth == max_depth:
        return 0

    if is_max:
        return max(minimax(stones-m, False, depth+1, max_depth)
                   for m in [1,2] if stones-m >= 0)
    else:
        return min(minimax(stones-m, True, depth+1, max_depth)
                   for m in [1,2] if stones-m >= 0)

def best_move(stones, depth, explain):
    best, move = -math.inf, None
    for m in [1,2]:
        if stones-m >= 0:
            val = minimax(stones-m, False, 0, depth)
            if explain:
                print(f"Try {m} -> {val}")
            if val > best:
                best, move = val, m
    return move, best

# ----------------------------
# LOOP: Prompt → Update Output
# ----------------------------
stones = 5
print("Game: Remove 1 or 2 stones. Last wins.")
print("Initial stones:", stones)

while True:
    prompt = input("\nEnter prompt (or 'exit'): ").lower()
    if prompt == "exit":
        break

    # parse prompt
    depth = 3 if "depth=3" in prompt else 2
    explain = "explain" in prompt

    move, score = best_move(stones, depth, explain)

    print("👉 Updated Result:")
    print("Best move:", move, "| Score:", score)