# Practical 8: Semantic Network using Predicate Logic

# Predicate functions
def isa(x, y):
    return f"{x} is a {y}"

def has(x, y):
    return f"{x} has {y}"

def can(x, action):
    return f"{x} can {action}"

# Knowledge Base
knowledge_base = [
    isa("Bird", "Animal"),
    isa("Dog", "Animal"),
    isa("Sparrow", "Bird"),
    has("Animal", "Cells"),
    can("Bird", "Fly"),
    can("Dog", "Bark")
]

print("Semantic Network Representation:\n")

for fact in knowledge_base:
    print(fact)