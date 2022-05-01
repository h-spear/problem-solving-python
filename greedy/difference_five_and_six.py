a, b = input().split()

max_a = int(a.replace("5", "6"))
max_b = int(b.replace("5", "6"))
min_a = int(a.replace("6", "5"))
min_b = int(b.replace("6", "5"))

print(min_a + min_b, max_a + max_b)
