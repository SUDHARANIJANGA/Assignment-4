num = (1, 2, 3, 4, 5, 6, 7)
print("Original list: ", num)
result = map(lambda x: x + x + x, num)
print("\nTriple of said list numbers :")
print(list(result))
