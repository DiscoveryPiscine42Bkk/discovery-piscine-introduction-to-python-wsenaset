
def main():
    original = [2, 8, 9, 48, 8, 22, -12, 2]
    new = [x + 2 for x in original if x > 5]

    print(original, end='')
    print()
    print(new)
main()