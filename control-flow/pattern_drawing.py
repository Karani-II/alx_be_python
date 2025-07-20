pattern_size = int(input("Enter the size of the pattern:"))
while pattern_size < 1:
    print("size must be greater than 0")
    pattern_size = int(input("Enter the size of the pattern:"))
for i in range(pattern_size):
        for j in range(pattern_size):
            print("*", end="")
        print()
