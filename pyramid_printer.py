height = int(input("Enter the height of the pyramid: "))

for level in range(1, height + 1):
    for _ in range(height - level):
        print(" ", end="")
    for _ in range(2 * level - 1):
        print("#", end="")
    print()
