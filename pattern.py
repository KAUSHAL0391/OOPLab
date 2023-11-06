def display_pattern(num_rows):
    for i in range(1, num_rows + 1):
        print(f"Row {i}:", end=" ")
        for j in range(i):
            print("*", end=" ")
        print()
if __name__ == "__main__":
    num_rows = int(input("Enter the number of rows for the pattern: "))
    display_pattern(num_rows)