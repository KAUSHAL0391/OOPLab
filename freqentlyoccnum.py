def most_frequent_number(numbers):
    frequency_count = {}
    for num in numbers:
        if num in frequency_count:
            frequency_count[num] += 1
        else:
            frequency_count[num] = 1
    most_frequent = max(frequency_count, key=frequency_count.get)
    return most_frequent
if __name__ == "__main__":
    input_numbers = input("Enter a list of numbers separated by spaces: ")
    numbers = list(map(int, input_numbers.split()))
    most_frequent_num = most_frequent_number(numbers)
    print(f"The most frequently occurring number in the list is: {most_frequent_num}")