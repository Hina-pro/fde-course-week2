"""import copy

original = [[100, 200], [300, 400]]

copied = copy.deepcopy(original)

copied[0][0] = 999

print(original)
print(copied)"""

# Example # 2

original = [100, 200, 300]
copied = original.copy()

copied[0] = 999

print(original)
print(copied)
