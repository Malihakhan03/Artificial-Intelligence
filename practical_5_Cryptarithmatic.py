import itertools

def solve_cryptarithmetic(word1, word2, result):
    chars = set(word1 + word2 + result)
    if len(chars) > 10:
        return None

    unique_chars = list(chars)
    leading_chars = {word1[0], word2[0], result[0]}

    for perm in itertools.permutations(range(10), len(unique_chars)):
        char_to_digit = dict(zip(unique_chars, perm))

        # Skip if any leading character is assigned zero
        if any(char_to_digit[ch] == 0 for ch in leading_chars):
            continue

        num1 = int("".join(str(char_to_digit[c]) for c in word1))
        num2 = int("".join(str(char_to_digit[c]) for c in word2))
        res = int("".join(str(char_to_digit[c]) for c in result))

        if num1 + num2 == res:
            return num1, num2, res

    return None


# --------- USER INPUT PART ---------
word1 = input("Enter first word: ").upper()
word2 = input("Enter second word: ").upper()
result = input("Enter result word: ").upper()

solution = solve_cryptarithmetic(word1, word2, result)

if solution:
    print("\nSolution found:")
    print(f" {word1:<8} ({solution[0]})")
    print(f"+ {word2:<8} ({solution[1]})")
    print("-----------")
    print(f"= {result:<8} ({solution[2]})")
else:
    print("\nNo solution found.")